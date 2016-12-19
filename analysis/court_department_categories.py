
# todo: create a unittest from this list (check that every list entry is tagged correctly)
department_mapping = {
    'Administrative Law': [
        'Eidg. Schätzungskommission',
        'Camera di diritto amministrativo',
        'Internen Rekurskommission des Bundesgerichts',
        'Verwaltungskommission',
        'la Chambre de droit administratif',
        'verwaltungsrechtlichen Kammer'
    ],
    'Private Law': [
        '1. Zivilabteilung',
        'H. Zivilabteilung',
        'I Camera civile',
        'I Corte Civile',
        'I Corte civile',
        'I Corte di diritto civile',
        'I. Corte civile',
        'I. Zivilabteilung',
        'I. Zivilabtellung',
        'I. zivilrechtlichen Abteilung',
        'I. Zlvilabteilung',
        'I. Zlvilabtellung',
        'II Camera civile',
        'II Corte Civile',
        'II Corte civile',
        'II Corte di diritto civile',
        'II. Corte civile',
        'II. Zivilabteilung',
        'II. Zivilabtellung',
        'II. Zivllabteilung',
        'II. Zlvilabteilung',
        'II. zivilrechtlichen Abtei- lung',
        'II. zivilrechtlichen Abteilung',
        'III. Zivilabteilung',
        'Ia Corte civile',
        'Ia Ire Cour civile',
        'Ia. Zivilabteilung',
        'Il. Zivilabteilung',
        'Präsidenten der I. Zivilabteilung',
        'Präidenten der II. Zivilabteilung',
        'Präsidenten des Bundesgerichts',
        'Zivilabteilung',
        'ai Corte civile',
        'la Corte civile',
        'la He Cour civile'
        'la I/e Cour civile',
        'la IIe CCivile',
        'la IIe Cour Civile',
        'la IIe Cour civile',
        'la IIe Cour civile, du',
        'la IIe Cour civlle',
        'la IIe Cour de droit civil',
        'la IIe cour civile',
        'la IIème Cour civile',
        'la Ie Cour Civile',
        'la Ie Cour civile',
        'la Ie Cour clvile',
        'la Ile Cour civile',
        'la Ile cour civile',
        'la Ire Cour Civile',
        'la Ire Cour civile',
        'la Ire Cour civlle',
        'la Ire Cour de droit civil',
        'la Ire cour civile'
        'la Ire cour civile, du'
        'la Ière Cour civile',
        'la le Cour civile'
    ],
    'Public Law': [
        '1. Öffentlichrechtlichen Abteilung',
        'I Corte di diritto pubblico',
        'I. Zivilabteilung als Staatsgerichtshofs',
        'I. Zivilabteilung als staatsrechtliche Kammer',
        'I. Zivilabteilung als staatsrechtlicher Kammer',
        'I. partiziun da dretg public',
        'I. Öffentlichrechtlichen Abteilung',
        'I. Öffentlich-rechtlichen Abteilung',
        'I. Öffentlichrechtilchen Abteilung',
        'I. Öffentlichrechtlicben Abteilung',
        'I. Öffentlichrechtlichen Ab- teilung',
        'I. Öffentlichrechtlichen Abteilung',
        'II Corte di diritto pubblico',
        'II. OerA',
        'II. Zivilabteilung als Staatsgerichtshof',
        'II. Zivilabteilung als Staatsgerichtshofs',
        'II. Zivilabteilung als Staatsrechtlicher Kammer',
        'II. Zivilabteilung als staatsrechtliche Kammer',
        'II. Zivilabteilung als staatsrechtlicher Kammer',
        'II. Öffentlichrechtlichen Abteilung',
        'II. Öffentlich-rechtlichen Abtei- lung',
        'II. Öffentlich-rechtlichen Abteilung',
        'II. Öffentlichrechtlichen Abtei- lung',
        'II. Öffentlichrechtlichen Abteilung',
        'Ia Corte di diritto pubblico',
        'Instruktionsrichters',
        'Präsidenten der I. Öffentlichrechtlichen Abteilung',
        'Präsidenten der II. Öffentlichrechtlichen Abteilung',
        'la Chambre de droit public',
        'la IIe Cour civile statuant comme Chambre de droit public',
        'la IIe Cour civile statuant comme chambre de droit public',
        'la IIe Cour civile, statuant comme Chambre de droit public, du',
        'la IIe Cour de droit public',
        'la IIe cour de droit public',
        'la IIème Cour de droit public',
        'la Ie Cour de droit public',
        'la Ire Cour civile (comme chambre de droit public) du',
        'la Ire Cour civile statuant comme Chambre de droit public',
        'la Ire Cour de droit public',
        'la Ire cour de droit public',
        'la Ière Cour de droit public',
        'la chambre de droit public',
        'la cour de cassation pénale statuant comme Chambre de droit public, du',
        'Kassationshofes als staatsrechtlicher Kammer',
        'staatsrechtlichen Abteilung',
        'staatsrechtlichen Kammer',
    ],
    'Criminal Law': [
        "Angeklagekammer",
        "Anklagekammer",
        "Bundesstrafgerichtes",
        "Bundesstrafgerichts",
        "Camera d'accusa",
        "Camera d'accusa del Tribunale federale",
        "Camera di accusa",
        'Corte di Cassazione penale',
        'Corte di cassazione',
        'Corte di cassazione penale',
        'Corte di diritto penale',
        'Corte di eassazione penale',
        'Kassationsbofes',
        'Kassationshofcs',
        'Kassationshofes',
        'Kassationshofs',
        'Kassationsholes',
        'Kassatlonshofes',
        'Strafrechtlichen Abteilung',
        'ausserordentlichen Kassationshofes',
        "camera d'accusa",
        "la Chambre d'accusation",
        'la Cour de cassation',
        'la Cour de cassation penale',
        'la Cour de cassation pénale',
        'la Cour de cassation pénale du Il septembre',
        'la Cour de cassation pénale, du',
        'la Cour de cassatlon pénale',
        'la Cour de droit pénal',
        'la Cour pénale fédérale',
        'la cassation pénale',
        'la cour de cassation pénale',
        'la cour de cassation pénale, du'
    ],
    'Debt Recovery and Bankruptcy': [
        'Camera delle esecuzioni e dei fallimenti',
        'Schuldbetreibungs- und Kon-kurskammer',
        'Schuldbetreibungs- und Konkurs- kammer',
        'Schuldbetreibungs- und Konkurs-kammer',
        'Schuldbetreibungs- und Konkurskammer',
        'la Chambre des poursuites et des faillites',
        'la Chambre des poursuites et des faillites du Tribunal fédéral',
        'la Chambre des poursuites et faillites',
    ],
    'Social Insurance Law': [
        'Eidgenössischen Versicherungs-gerichts',
        'Eidgenössischen Versicherungsgerichts',
        'I Corte di diritto sociale',
        'I. sozialrechtlichen Abteilung',
        'II Corte di diritto sociale',
        'II. sozialrechtlichen Abteilung',
        'la IIe Cour de droit social',
        'la Ire Cour de droit social',
        'setenza della II Corte di diritto sociale'
    ]
}