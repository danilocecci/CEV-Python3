import colorama
colorama.init()

schema_colorama = {
    'close':'\033[m',

    'normal':'\033[0;30m',
    'normal_red':'\033[0;31m',
    'normal_green':'\033[0;32m',
    'normal_yellow':'\033[0;33m',
    'normal_blue':'\033[0;34m',
    'normal_purple':'\033[0;35m',
    'normal_cyan':'\033[0;36m',
    'normal_gray':'\033[0;37m',

    'bold':'\033[1;30m',
    'bold_red':'\033[1;31m',
    'bold_green':'\033[1;32m',
    'bold_yellow':'\033[1;33m',
    'bold_blue':'\033[1;34m',
    'bold_purple':'\033[1;35m',
    'bold_cyan':'\033[1;36m',
    'bold_gray':'\033[1;37m',

    'underline':'\033[4;30m',
    'underline_red':'\033[4;31m',
    'underline_green':'\033[4;32m',
    'underline_yelow':'\033[4;33m',
    'underline_blue':'\033[4;34m',
    'underline_purple':'\033[4;35m',
    'underline_cyan':'\033[4;36m',
    'underline_gray':'\033[4;37m',

    'inverted':'\033[7;30m',
    'inverted_red':'\033[7;31m',
    'inverted_green':'\033[7;32m',
    'inverted_yellow':'\033[7;33m',
    'inverted_blue':'\033[7;34m',
    'inverted_purple':'\033[7;35m',
    'inverted_cyan':'\033[7;36m',
    'inverted_gray':'\033[7;37m'
}


print('\033[32mOlá, Mundo!\033[m')
print('Feito com {}amor{}!'.format(schema_colorama['normal_red'], schema_colorama['close']))