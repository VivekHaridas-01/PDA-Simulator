from lang import Languages
from argparse import ArgumentParser, RawTextHelpFormatter

if __name__ == "__main__":
    l = Languages()
    parser = ArgumentParser(
        description="PushDown Automata Simulator", allow_abbrev=False, formatter_class=RawTextHelpFormatter
    )
    # Flag to be specified to select language to be loaded
    parser.add_argument('-i', "--input", action = 'store', type = str, required = "True",
                        help="""Enter the language you want:
L = {aNbN : N >= 0}             -      1
L = {aNb2N : N >= 0}            -      2
L = {aMbNc(M+N) : M,N >= 0}     -      3
L = {aNbMcMdN : M,N >= 0}       -      4
L = {wcwR : w ∈ (a+b)*}         -      5
L = {wwR : w ∈ (a+b)*}          -      6
"""
    )
    args = parser.parse_args()

    maps = {
        '1': 'aNbN',
        '2': 'aNb2N',
        '3': 'aMbNcM+N',
        '4': 'aNbMcMdN',
        '5': 'wcwR',
        '6': 'wwR'
    }

    pda = l.get_lang(maps[args.input])

    pda.exec(input("Enter string to validate: "))
