letters = {
    'K': [
        '*     *',
        '*   *  ',
        '* *    ',
        '**     ',
        '* *    ',
        '*   *  ',
        '*     *'
    ],
    'U': [
        '*    *',
        '*    *',
        '*    *',
        '*    *',
        '*    *',
        '*    *',
        ' **** '
    ],
    'Y': [
        '*     *',
        ' *   * ',
        '  * *  ',
        '   *   ',
        '   *   ',
        '   *   ',
        '   *   '
    ],
    ' ': [
        '     ',
        '     ',
        '     ',
        '     ',
        '     ',
        '     ',
        '     '
    ],
    'S': [
        '  *** ',
        ' *    ',
        ' *    ',
        '  *** ',
        '     *',
        ' *   *',
        '  *** '
    ],
    'I': [
        ' ***** ',
        '   *   ',
        '   *   ',
        '   *   ',
        '   *   ',
        '   *   ',
        ' ***** '
    ],
    'T': [
        '*******',
        '   *   ',
        '   *   ',
        '   *   ',
        '   *   ',
        '   *   ',
        '   *   '
    ],
    'C': [
        '  **** ',
        ' *    *',
        '*      ',
        '*      ',
        '*      ',
        ' *    *',
        '  **** '
    ],
    'H': [
        '*    *',
        '*    *',
        '*    *',
        '******',
        '*    *',
        '*    *',
        '*    *'
    ],
    'A': [
        '   *   ',
        '  * *  ',
        ' *   * ',
        '*******',
        '*     *',
        '*     *',
        '*     *'
    ]
}

def print_word(word):
    for i in range(7):
        line = ''
        for j in range(len(word)):
            line += letters[word[j]][i] + '  '
        print(line)

print_word('KUY SITTICHAI')
