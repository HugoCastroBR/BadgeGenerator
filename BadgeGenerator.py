# utf-8
# by Hugo Castro
# only sys.argv and python 3.8
# coded in VsCode


from sys import argv


class shield(): # class of order
    toGen = []
    
    def __init__(self,logo = None,color = None,style = None,subject = None,status = None,features = None):
        # catch features
        self.features ={ 
            "logo":logo,
            "color":color,
            "style":style,
            "subject":subject,
            "status":status
        }

        # transform some style and color in lowercase
        if type(self.features["color"] ) == str:
            self.features["color"] = self.features["color"].lower()
        if type(self.features["style"] ) == str:
            self.features["style"] = self.features["style"].lower()

    def verify(self,whattoverify,list = [" ",""] ): #verify if have some character not supported

        if type(whattoverify) == list or type(whattoverify) == dict:
            for element in whattoverify:
                if element in list:
                    return False
        else:
            if whattoverify in list:
                return False
        return True

    def generate(self): # verify infos and generate a link
        firstime = True
        todel = []
        template = "https://img.shields.io/badge/"
        self.link = "https://img.shields.io/badge/"
        for element in self.features :
            if self.features[element] in [" ",""] or type(self.features[element]) != str:
                todel.append(self.features[element])

        for el in todel:
            if el in self.features:
                self.features[el] == None
                
        if self.features["subject"] != None:
            if self.verify(self.features["subject"]) == True:
                self.link += f"{self.features['subject']}"

        if self.features["status"] != None:
            if self.verify(self.features["status"]) == True:
                self.link += f"{self.features['status']}"

        if self.features["color"] != None:
            if self.verify(self.features["color"]) == True:
                if self.features["status"] != None or self.features["subject"] != None:

                    if self.verify(self.features["status"]) == True or self.verify(self.features["subject"]):
                        self.link += f"-{self.features['color']}"

                    else:
                        self.link += f"--{self.features['color']}"

                else:
                    self.link += f"--{self.features['color']}"

        if self.features["color"] != None:
            if self.verify(self.features["color"]) == True: 
                self.link += f".svg?"
            else:
                self.link += f"-%20.svg?"
        else:
            self.link += f"-%20.svg?"

        if self.features["style"] != None:
            if self.verify(self.features["style"]) == True:
                self.link += f"style={self.features['style']}"

        if self.features["logo"] != None:
            if self.verify(self.features["logo"]) == True:
                self.link += f"&logo={self.features['logo']}"
        
            
    def fresh(self): # valid a link 
        self.generate()
        self.link_words = list(self.link)
        self.i = 0

        for word in self.link_words:
            
            if word == " ":
                self.link_words[self.i] = "%20"
            self.i+=1

        self.link = ""

        for word in self.link_words:
            
            self.link += word

    def __str__(self): # print your link
        self.fresh()
        return print(f"\nhere is your link bud: {self.link}")
    
def print_help():
    print("\n#You can run with shell commands")
    print("#-Ex:\n#main.py -s flat --color red")
    print("#Commands:")
    print("#-h or --help to see this message again")
    print("#-s or --style to set a style like: flat, plastic, flat-square, for-the-badge or social.")
    print("#-c or --color to set a style like: Black, Blue, Red, Gray, and others.")
    print("#-t , -su or --subject, -title to define a title/subject of your badge.")
    print("#-st , -m or --status, --message to define a status/message of your badge.")
    print("#-l or --logo to define a logo like : django, python, javascript, and others (just try).\n")

def check_args(): #check args and apply
    index = 0
    args = {  #list of supported args
        "-s":"--style", 
        "-c":"--color",
        "-m":"--message",
        "-st":"--status",
        "-su":"--subject",
        "-t":"--title",
        "-l":"--logo",
        "-h":"--help"
    }
    features = {"style": None, # features which you can change the pattern if you want 
                "color": None,
                "status": None,
                "subject":None,
                "logo":None
    }
    for arg in argv: # scan every arg
        arg = arg.lower() # transform each arg to lowercase
        if arg in args:
            try: 
                if argv[index+1]  in args: 
                    print(f"Arguments of '{argv[index]}' are required ") 
                    print_help()
                else:
                    if arg == "-s" or arg == "--style":
                        features["style"] = argv[index+1]

                    elif arg == "-c" or arg == "--color":
                        features["color"] = argv[index+1]
                    
                    elif (arg == "-st" or arg == "--status") or (arg == "-m" or arg == "--message"):
                        features["status"] = argv[index+1]

                    elif (arg == "-su" or arg == "--subject") or (arg == "-t" or arg == "--title"):
                        features["status"] = argv[index+1]

                    elif arg == "-l" or arg == "--logo":
                        features["logo"] = argv[index+1]

                    elif arg == "-h" or arg == "--logo":
                        print_help()

            except: # don't be afraid if its working bud
                pass

        index += 1 #classic index
        #create a object with the args
    try:
        print(shield( 
        style=features['style'],
        color=features['color'],
        status=features['status'],
        logo=features['logo'],
        subject=features['subject']
        ))
    except:
        pass
    
    
def shell_type():
    print("[just press Enter if you don't want to put something in some input]")
    #create a object with the args
    try:
        print(shield( 
        style=input("Style: "),
        color=input("Color: "),
        status=input("Status: "),
        logo=input("Logo: "),
        subject=input("Subject: ")
        ))
    except TypeError: # sorry i don't know what to do here
        pass

def main():
    print("#coded by Hugo Castro") 
    # its me if you want
    # mail me hugocastrohc@outlook.com

    print("#Brazil +55 032\n")

    
    

    if len(argv) <= 2: # verify wheather have args
        print_help()

        shell_type() # if don't have args go with shell type


    else: # if have args go to use it
        check_args()
main()

print("\n")


