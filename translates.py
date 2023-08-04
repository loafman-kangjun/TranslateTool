from translate import Translator

languages = ['af-ZA', 'sq-AL', 'am-ET', 'ar-SA', 'hy-AM', 'az-AZ', 'bjs-BB', 'rm-RO', 'eu-ES', 'bem-ZM', 'bn-IN',
             'be-BY', 'bi-VU', 'bs-BA', 'br-FR', 'bg-BG', 'my-MM', 'ca-ES', 'ceb-PH', 'ch-GU', 'zdj-KM', 'cop-EG',
             'pov-GW', 'hr-HR', 'cs-CZ', 'da-DK', 'nl-NL', 'dz-BT', 'eo-EU', 'et-EE', 'fn-FNG', 'fo-FO', 'fi-FI',
             'fr-FR', 'gl-ES', 'ka-GE', 'de-DE', 'el-GR', 'grc-GR', 'gu-IN', 'ha-NE', 'haw-US', 'he-IL', 'hi-IN',
             'hu-HU', 'is-IS', 'id-ID', 'kl-GL', 'ga-IE', 'it-IT', 'ja-JP', 'jv-ID', 'kea-CV', 'kab-DZ', 'kn-IN',
             'kk-KZ', 'km-KM', 'rw-RW', 'rn-BI', 'ko-KR', 'ku-TR', 'ckb-IQ', 'ky-KG', 'lo-LA', 'la-VA', 'lv-LV',
             'lt-LT', 'lb-LU', 'mk-MK', 'mg-MG', 'ms-MY', 'dv-MV', 'mt-MT', 'gv-IM', 'mi-NZ', 'mh-MH', 'men-SL',
             'mn-MN', 'mfe-MU', 'ne-NP', 'niu-NU', 'no-NO', 'ny-MW', 'ur-PK', 'pau-PW', 'pa-IN', 'pap-CW', 'ps-PK',
             'fa-IR', 'pis-SB', 'pl-PL', 'pt-PT', 'pot-US', 'qu-PE', 'ro-RO', 'ru-RU', 'sm-WS', 'sg-CF', 'gd-GB',
             'sr-RS', 'sn-ZW', 'si-LK', 'sk-SK', 'sl-SI', 'so-SO', 'st-ST', 'es-ES', 'srn-SR', 'sw-SZ', 'sv-SE',
             'de-CH', 'syc-TR', 'tl-PH', 'tg-TJ', 'tmh-DZ', 'ta-LK', 'te-IN', 'tet-TL', 'th-TH', 'bo-CN', 'ti-TI',
             'tpi-PG', 'tkl-TK', 'to-TO', 'tn-BW', 'tr-TR', 'tk-TM', 'tvl-TV', 'uk-UA', 'ppk-ID', 'uz-UZ', 'vi-VN',
             'wls-WF', 'cy-GB', 'wo-SN', 'xh-ZA', 'yi-YD', 'zu-ZA']


def fanyi(src, email, flang, tlang):
    __translator = Translator(from_lang=flang, to_lang=tlang, email=email, provider="mymemory")
    __translation = __translator.translate(src)
    return __translation


if __name__ == '__main__':
    translator = Translator(from_lang="zh-CN", to_lang="tl-PH", email="kangjun1120@126.com", provider="mymemory")
    translation = translator.translate("床前明月光，疑是地上霜;举头望明月,低头思故乡")
    print(translation)
