"""argparse"""


def get_args(parser):
    """Define every input parameter when running the main script.
    :param parser:
    :return:
    """
    # only many times args
    parser.add_argument("-v", "--verbose", action='store_true',
                        help="""Verbose mode, more log messages""")
    parser.add_argument('--src-dir', dest='src_dir', default="src", type=str,
                        help='directory for source code')
    parser.add_argument('--submit', dest='submit', action='store_true',
                        help='whether to submit when all test are passed.')
    parser.add_argument('--mkdir', dest='mkdir', action='store_true',
                        help='whether to make directory and source code.')
    parser.add_argument('--prob', dest='prob', type=str, choices=list("abcdef"),
                        help="choices : a,b,c,d,e,f")
    parser.add_argument('--level', dest='level', default="abc", type=str, choices=["abc", "arc", "agc"],
                        help='choices : abc,arc,agc')
    parser.add_argument('--rnd', dest='rnd', type=int,
                        help='int')
    parser.add_argument('--lang', dest='lang', default="python", type=str, choices=["python", "cpp"],
                        help='choices : python, cpp')