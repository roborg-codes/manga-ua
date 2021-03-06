import random
import questionary

def get_emoji(emotion):
    joy = ['(* ^ ω ^)','(´ ∀ ` *)','٩(◕‿◕｡)۶','☆*:.｡.o(≧▽≦)o.｡.:*☆','(o^▽^o)','(⌒▽⌒)☆','<(￣︶￣)>','。.:☆*:･\'(*⌒―⌒*)))','ヽ(・∀・)ﾉ','(´｡• ω •｡`)','(￣ω￣)','｀;:゛;｀;･(°ε° )','(o･ω･o)','(＠＾◡＾)','ヽ(*・ω・)ﾉ','(o_ _)ﾉ彡☆','(^人^)','(o´▽`o)','(*´▽`*)','｡ﾟ( ﾟ^∀^ﾟ)ﾟ｡','( ´ ω ` )','(((o(*°▽°*)o)))','(≧◡≦)','(o´∀`o)','(´• ω •`)','(＾▽＾)','(⌒ω⌒)','∑d(°∀°d)','╰(▔∀▔)╯','(─‿‿─)','(*^‿^*)','ヽ(o^ ^o)ﾉ','(✯◡✯)','(◕‿◕)','(*≧ω≦*)','(☆▽☆)','(⌒‿⌒)','＼(≧▽≦)／','ヽ(o＾▽＾o)ノ','☆ ～(\'▽^人)','(*°▽°*)','٩(｡•́‿•̀｡)۶','(✧ω✧)','ヽ(*⌒▽⌒*)ﾉ','(´｡• ᵕ •｡`)','( ´ ▽ ` )','(￣▽￣)','╰(*´︶`*)╯','ヽ(>∀<☆)ノ','o(≧▽≦)o','(☆ω☆)','(っ˘ω˘ς )','＼(￣▽￣)／','(*¯︶¯*)','＼(＾▽＾)／','٩(◕‿◕)۶','(o˘◡˘o)','\(★ω★)/','\(^ヮ^)/','(〃＾▽＾〃)','(╯✧▽✧)╯','o(>ω<)o','o( ❛ᴗ❛ )o','｡ﾟ(TヮT)ﾟ｡','( ‾́ ◡ ‾́ )','(ﾉ´ヮ`)ﾉ*: ･ﾟ','(b ᵔ▽ᵔ)b','(๑˃ᴗ˂)ﻭ','(๑˘︶˘๑)','°˖✧◝(⁰▿⁰)◜✧˖°','(´･ᴗ･ ` )','(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧','(„• ֊ •„)','(.❛ ᴗ ❛.)','(⁀ᗢ⁀)','(￢‿￢ )','(¬‿¬ )','(*￣▽￣)b','( ˙▿˙ )','(¯▿¯)','( ◕▿◕ )','＼(٥⁀▽⁀ )／']
    confusion = ['(￣ω￣;)','σ(￣、￣〃)','(￣～￣;)','(-_-;)・・・','┐(\'～`;)┌','(・_・ヾ','(〃￣ω￣〃ゞ','┐(￣ヘ￣;)┌','(・_・;)','(￣_￣)・・・','╮(￣ω￣;)╭','(¯ . ¯;)','(＠_＠)','(・・;)ゞ','Σ(￣。￣ﾉ)','(・・ ) ?','(•ิ_•ิ)?','(◎ ◎)ゞ','(ーー;)','ლ(ಠ_ಠ ლ)','ლ(¯ロ¯"ლ)','(¯ . ¯٥)','(¯ ¯٥)']
    pain = ['~(>_<~)','☆⌒(> _ <)','☆⌒(>。<)','(☆_@)','(×_×)','(x_x)','(×_×)⌒☆','(x_x)⌒☆','(×﹏×)','☆(＃××)','(＋_＋)','[ ± _ ± ]','٩(× ×)۶','_:(´ཀ`」 ∠):_']

    if emotion == "joy":
        item = random.randint(0, len(joy) - 1)
        return joy[item]
    elif emotion == "confusion":
        item = random.randint(0, len(confusion) - 1)
        return confusion[item]
    elif emotion == "pain":
        item = random.randint(0, len(pain) - 1)
        return pain[item]
    else:
        return

def check_volumes(manga_volumes):
    if not manga_volumes:
        questionary.print(f"Не вдалося завантажити манґу {get_emoji('pain')}", style="bold italic")
        exit(1)

def check_downloaded(downloaded):
    if not downloaded:
        questionary.print(f"Завантаження не пройшло успішно... {get_emoji('confusion')}", style="bold italic")
        exit(1)
    else:
        questionary.print(f"Завантажено успішно! {get_emoji('joy')}", style="italic")
        exit(0)

def check_search_results(search_results):
    if not search_results:
        questionary.print(f"Нічого не знайдено {get_emoji('confusion')}", style="italic")
        exit(0)
