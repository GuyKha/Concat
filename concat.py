from gooey import Gooey, GooeyParser

@Gooey(advanced=True,  
       program_name='name',       # Defaults to script name
       program_description = 'concatentor',       # Defaults to ArgParse Description
       default_size=(500, 350),   # starting size of the GUI
       required_cols=1,           # number of columns in the "Required" section
       optional_cols=1
    )   
def main():
    """ Use GooeyParser to build up the arguments we will use in our script
    Save the arguments in a default json file so that we can retrieve them
    every time we run the script.
    """
    parser = GooeyParser(description='Concatenation app')
    parser.add_argument('inputDir',action='store',widget='DirChooser',help="The directory that contains the files to concatenate")
    parser.add_argument('compress',action='store_true',widget='CheckBox',help='Compress')
    args = parser.parse_args()

# define main as start module
if __name__ == "__main__":
    main()
