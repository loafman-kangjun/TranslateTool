from translate import Translator

if __name__ == '__main__':
    translator = Translator(from_lang="zh-CN", to_lang="cu", email="kangjun1120@126.com", provider="mymemory")
    translation = translator.translate("床前明月光，疑是地上霜;举头望明月,低头思故乡")
    print(translation)
