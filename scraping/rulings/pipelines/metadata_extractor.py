# -*- coding: utf-8 -*-

import calendar
import locale
import re
import warnings


class MetadataExtractorPipeline(object):

    # get lists of month names in german, french and italian.
    # names are normalised: lower case + accents removed
    locale.setlocale(locale.LC_ALL, 'de_CH.utf8')  # todo: make sure that locale exists!
    months_de = [m.lower() for m in calendar.month_name]
    locale.setlocale(locale.LC_ALL, 'fr_CH.utf8')
    months_fr = [m.lower().replace('é', 'e').replace('û', 'u') for m in calendar.month_name]
    locale.setlocale(locale.LC_ALL, 'it_CH.utf8')
    months_it = [m.lower() for m in calendar.month_name]
    locale.setlocale(locale.LC_ALL, 'C')

    # for extracting the responsible department of the Federal Supreme Court
    department_patterns = {
        'de': r'(?:(?<=Urteil de\w )|(?<=Entscheid de\w )).*?(?= i.S.| vom \d)',
        'fr': r'(?<=arrêt de ).*?(?= dans la cause| du \d)',
        'it': r'(?<=della )(?!sentenza).*?(?= nella)'
    }

    # type of proceeding: in title of judgement; starts with '(', ends with ')' and does not contain any '(...)'
    type_of_proceeding_pattern = r'(?<=\().*?(?!.*\(.*\))(?=\))'

    # tokens for separating parties (also used for detecting the ruling's language)
    party_separator = {
        'de': {
            'start': 'i.S. ',
            'end': ' gegen '
        },
        'fr': {
            'start': 'dans la cause ',
            'end': ' contre '
        },
        'it': {
            'start': 'nella causa ',
            'end': ' contro '
        }
    }
    end_party_pattern = r'(?<=%s).*?'                  # starts after a party_separator (see above)
    end_party_pattern += r'(?:[^A-Z](?=\.\s?(?:\n|$))'  # if end of the sentence: don't include '.'
    end_party_pattern += r'|[A-Z]\.(?=\n|$)'            # if ending with abbr: include '.'
    end_party_pattern += r'|(?= \([^()]+\)(?:\n|$))'    # if ending with '(...)', don't include it (= proceeding type)
    end_party_pattern += r'|(?=\n|$))'                  # stop at newline at latest.

    def process_item(self, item, spider):
        url = item['url']
        item['date'] = self._extract_date(item['title_of_judgement'], url)
        item['dossier_number'] = self._extract_dossier_number(item['title_of_judgement'], url)
        item['department'] = self._extract_department(item['title_of_judgement'], url)
        item['involved_parties'] = self._extract_involved_parties(item['title_of_judgement'], url)
        item['language'] = self._extract_language(item['title_of_judgement'], url)
        item['type_of_proceeding'] = self._extract_type_of_proceeding(item['title_of_judgement'], url)
        return item

    def _extract_date(self, raw_date, url):
        # match 4-digit number if preceded by '.' or ' '
        year_match = re.search(r'(?<=[\.\s])\d{4}', raw_date)

        # if year was found, look for day and month
        if year_match is not None:
            year = int(year_match.group())

            # match one- or two-digit number preceded by ' ' and followed by '.' or ' ' or 'er' (-> premier)
            day_match = re.search(r'(?<=[\s\(\'])(\d{1,2})(\.\s?|\s|\w+ )', raw_date)
            day = int(day_match.group(1))

            # extract month (digit between 1 and 12)
            # month token is between day and year token extracted above
            month_start = day_match.span()[1]
            month_end = year_match.span()[0] - 1
            month_raw = raw_date[month_start:month_end].replace(' ', '').replace('.', '')
            month = None
            # if month is represented as digit, we're done
            if month_raw.isdigit():
                month = int(month_raw)
            # if month is represented as string, we need to find out, which month it is (german, french and italian)
            else:
                month_raw = month_raw.lower()

                # if it's french, remove accents
                month_raw = month_raw.replace('é', 'e').replace('û', 'u')

                if month_raw in self.months_de:
                    month = self.months_de.index(month_raw)
                elif month_raw in self.months_fr:
                    month = self.months_fr.index(month_raw)
                elif month_raw in self.months_it:
                    month = self.months_it.index(month_raw)

            if month is None:
                warnings.warn('Could not extract month. \nRuling: ' + url)
                # date = datetime(year, 1, 1)
                date = str(year)
            else:
                # date = datetime(year, month, day)
                date = '%02d.%02d.%04d' % (day, month, year)
            return date

    def _extract_involved_parties(self, raw_parties, url):
        # extract claimant and defendant
        for language, separator in self.party_separator.items():
            start_claimant = raw_parties.find(separator['start'])

            # if claimant indicator has been found...
            if start_claimant != -1:
                start_claimant += len(separator['start'])

                end_claimant = raw_parties.find(separator['end'])

                # if claimant and defendant can be separated...
                if end_claimant != -1:

                    # use end_party_pattern for extracting defendant
                    defendant = re.search(self.end_party_pattern % separator['end'], raw_parties).group()
                    parties = {
                        'claimant': raw_parties[start_claimant:end_claimant],
                        'defendant': defendant
                    }

                # otherwise there is only a claimant.
                else:
                    # use end_party_pattern for extracting claimant
                    claimant = re.search(self.end_party_pattern % separator['start'], raw_parties).group()
                    parties = {'claimant': claimant}

                return parties

        warnings.warn('Could not extract parties. \nRuling: ' + url)

    def _extract_dossier_number(self, raw_dossier_number, url):
        # extract 'Dossiernummer' (e.g. '5A_153/2009' or '4C.197/2003')
        # http://www.bger.ch/uebersicht_numm_dossiers_internet_d_ab_2007.pdf
        dnb_match = re.search('\d+\w+[\_\.]\d+\/\d{4}', raw_dossier_number)

        if dnb_match is not None:
            return dnb_match.group()

    def _extract_department(self, raw_department, url):
        # extract the responsible department if possible.
        for language, department_pattern in self.department_patterns.items():
            department_match = re.search(department_pattern, raw_department, re.IGNORECASE)
            if department_match is not None:
                return department_match.group()
        warnings.warn('Could not extract responsible department. \nRuling: ' + url)

    def _extract_type_of_proceeding(self, raw_type_of_proceeding, url):
        proceeding_match = re.search(self.type_of_proceeding_pattern, raw_type_of_proceeding)
        if proceeding_match is not None:
            return proceeding_match.group()
        warnings.warn('Could not extract the type of the proceeding. \nRuling: ' + url)

    def _extract_language(self, raw_parties, url):
        # language can be extracted if claimant and defendant can be extracted
        for language, separator in self.party_separator.items():
            start_claimant = raw_parties.find(separator['start'])
            end_claimant = raw_parties.find(separator['end'])

            # if claimant and defendant can be separated, language is known.
            if start_claimant != -1 and end_claimant != -1:
                return language

        warnings.warn('Could not extract language. \nRuling: ' + url)
