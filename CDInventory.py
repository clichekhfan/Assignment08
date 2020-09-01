#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# AHanson, 2020-Aug-31, add more psudocode to outline
# AHanson, 2020-Aug-31, created classes, methods, and functions
# AHanson, 2020-Aug-31, created main body code
# AHanson, 2020-Aug-31, added load option
# AHanson, 2020-Aug-31, added delete option
# AHanson, 2020-Aug-31, fixed bugs with properties
# AHanson, 2020-Aug-31, labeled load_inventory and save_inventory with type hints
# AHanson, 2020-Aug-31, labeled all functions and classes with placeholder docstring
# AHanson, 2020-Aug-31, updated docstring
#------------------------------------------#

import pickle

# -- DATA -- #
strChoice = '' # User input
strFileName = 'CDInventory.dat' # data storage file
lstOfCDObjects = [] #list of CD class objects
objFile = None  # file object

class CD:
    """ Stores data about a CD. 

        fields: __numCDs
        Attributes: (ID,title,artist)
        properties: (__ID,__title,__artist)
        Methods: (CDs,__incrementer,__atributestrings,__str__)"""

    #fields#
    __numCDs = 0 #this is the private variable for the number of CD objects instatiated

    #constructor#
    def __init__(self, i, t, a): # (i,t,a) are positional arguments that stand for ID, title, and artist
        """ Initializes the CD object.
            This method is implicitly called when the CD class is called with no other method.

            Attributes: (ID,title,artist)
                ID (integer): This is the numeric lable for the CD.
                title (string): This is the song title for the CD.
                artist (string): This is the artist of the song for the CD.

            Returns: instantiated CD class object"""

        #atributes#
        self.ID = i
        self.title = t
        self.artist = a
        CD.__incrementer() #this function increments the tracker for instatiated CD objects

    #properties#
    @property # cd_id: (int) with CD ID
    def ID(self):
        """ This is the getter property for the ID atribute. """
        return self.__ID
    @ID.setter
    def ID(self, value):
        """ This is the setter property for the ID atribute. """
        if type(value) != int:
            raise Exception('The CD ID must be an integer!')
        else:
            self.__ID = value

    @property #cd_title: (string) with the title of the CD
    def title(self):
        """ This is the getter property for the title atribute. """
        return self.__title
    @title.setter
    def title(self, value):
        """ This is the setter property for the title atribute. """
        if type(value) != str:
            raise Exception('The title must be a string!')
        #TODO: add duplicate entry check
        else:
            self.__title = value

    @property #cd_artist: (string) with the artist of the CD
    def artist(self):
        """ This is the getter property for the artist atribute. """
        return self.__artist
    @artist.setter
    def artist(self, value):
        """ This is the setter property for the artist atribute. """
        if type(value) != str:
            raise Exception('The artist must be a string!')
        else:
            self.__artist = value

    #methods#
    @staticmethod
    def CDs():
        """ This function returns the number of initialized CDs
        
            Args: None
                
            Returns: f'there are {CD.__numCDs} CD(s)'      """
        return f'there are {CD.__numCDs} CD(s)'

    @staticmethod
    def __incrementer():
        """ This function increments the number of initialized CDs """
        CD.__numCDs += 1

    def __atributestrings(self):
        """ this function returns a formated string containing the CDs atributes """
        return f"{self.__ID} - {self.__title} - {self.__artist}"

    def __str__(self):
        """ This customizes the dunder string function for this class
            This function calls the __atributestrings function """
        return self.__atributestrings()

# -- PROCESSING -- #

class FileIO:
    """ Processes data to and from file. """
    #fields#

    #constructor#

        #attributes#

    # properties:

    # methods:

    @staticmethod # save_inventory(file_name, lst_Inventory): -> None
    def save_inventory(file_name : str, lst_Inventory : list) -> None:
        """Function writes inventory to file

        opens the file
        takes in the inventory list
        writes a python object using pickle to a data file in binary format.
        closes file
        checks for genneral error and prints to user

        Args:
            file_name (string): name of file used to read the data from
            lst_Inventory (list of objects): 2D data structure (list of objects) that holds the data during runtime

        Returns:
            None.
        """
        with open(file_name, 'wb') as objFile:
           try:
               pickle.dump(lst_Inventory, objFile)
           except Exception as e:
               print(e)

    @staticmethod
    def load_inventory(file_name: str) -> list: # load_inventory(file_name): -> (a list of CD objects)
        """Function to manage data ingestion from file

        Reads the data from file identified by file_name into a list of objects
        (list of CD objects) list one item in the list represents one CD object.
        Checks for error with empty file.

        Args:
            file_name (string): name of file used to read the data from
            table (list of CD objetcs): 2D data structure (list of objects) that holds the data during runtime

        Returns:
            table.
        """
        table = []  # this clears existing data and allows to load data from file
        with open(file_name, 'rb') as objFile:
            try:
                table = pickle.load(objFile) #note: load() loads one line of data
            except (EOFError):
                print('Data file is empty!'.upper())
            except Exception as e:
                print (e)
        return table

class DataProcessor:
    ''' processses data within memory durring runtime '''

    #fields#

    #constructor#

        #attributes#

    # properties:

    # methods:

    @staticmethod
    def delete_entry(ID, table):
        """Deletes an entry from memory.
                    Modifies table to remove selected entry.

        Args:
            table (list of CD objects): 2D data structure (list of objects) that holds the data during runtime
            ID (integer): numerical ID for CD entry
            
        Returns:
            None.
        """
        intRowNr = -1
        blnCDRemoved = False
        for row in table:
            intRowNr += 1
            if row.ID == ID:
                del table[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')

# -- PRESENTATION (Input/Output) -- #
class IO:
    """ manages IO operations """

    #fields#

    #constructor#

        #attributes#

    # properties:

    # methods:

    @staticmethod
    def add():
        """
        takes initial user input
        checks that the ID entry is an Integer before return.
        loops until input is 'back'
        returns the user's inputs as a list of tuples.

        Args:
            None.

        Returns:
            lstTplUserinput (list of tuples): 2D data structure (list of tuples) that holds multiple user input tuples.

        """
        print('input "BACK" to exit')
        Userinputs = []
        while True:
            while True:
                strID = input('Enter ID: ').strip()
                if strID.upper().strip() == 'BACK':
                    break
                try:
                    int(strID)
                    break
                except(ValueError):
                    print('Invalid entry, please enter a number.')
                    continue
                except Exception as e:
                    print(e)
                    print('Please, try again.')
                    continue
            if strID.lower().strip() == 'BACK':
                break
            strTitle = input('What is the CD\'s title? ').strip()
            if strTitle.lower().strip() == 'BACK':
                break
            strArtist = input('What is the Artist\'s name? ').strip()
            if strArtist.lower().strip() == 'BACK':
                break
            tplUserinputs = (strID,strTitle,strArtist)
            Userinputs.append(tplUserinputs)
            print('input "BACK" to exit')
        return Userinputs
    
    @staticmethod
    def show_inventory(lis):
        #TODO update docstring
        """displays current inventory to user in console


        Args:
            lis (list of CDobjects): 2D data structure (list of CDobjects) that holds the data during runtime.

        Returns:
            None.

        """
        table = []
        for CDobj in lis:
            intID = CDobj.ID
            strTitle = CDobj.title
            strArtist = CDobj.artist
            dicRow = {'ID': intID, 'Title': strTitle, 'Artist': strArtist}
            table.append(dicRow)

        table = sorted(table, key = lambda i: i['ID']) 
        # https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-lambda-function/
        # https://www.youtube.com/watch?v=3dt4OGnU5sM

        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')

    @staticmethod
    def print_menu():
        """displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[LOAD] load Inventory from file\n[ADD] Add CD\n[SHOW] display Current Inventory')
        print('[DEL] delete CD from Inventory\n[SAVE] Save Inventory to file\n[EXIT] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): an upper case sting of the users input out of the choices LOAD, ADD, SHOW, DEL, SAVE or EXIT

        """
        choice = ' '
        while choice not in ['LOAD', 'ADD', 'SHOW', 'DEL', 'SAVE', 'EXIT']:
            choice = input('Which operation would you like to perform? [LOAD, ADD, SHOW, DEL, SAVE or EXIT]: ').upper().strip()
            if choice not in ['LOAD', 'ADD', 'SHOW', 'DEL', 'SAVE', 'EXIT']:
                print("Invalid input, try again!")
        print()  # Add extra space for layout
        return choice

# -- Main Body of Script -- #
# Load data from file into a list of CD objects on script start
# 1.0 Create inventory file if none exists
try:
    with open(strFileName, 'a') as objFile:
        pass
except Exception as e:
    print(e)
    print(type(e), e, e.__doc__, sep = '\n')
    print('CDInventory.dat file could not be acccessed or created, please contact support!')
    print('Program will not function properly without file access!')
    print("Please take notes so the problem can be recreated!")

# 1.1 When program starts, read in the currently saved Inventory
lstOfCDObjects = FileIO.load_inventory(strFileName)

# SHOWlay menu to user
while True:

    # 2.1 display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # let user exit program
    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'EXIT':
        break

        # show user current inventory
    # 3.2 process display current inventory
    elif strChoice == 'SHOW':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

        # let user add data to the inventory
    # 3.3 process add a CD
    elif strChoice == 'ADD':

        # 3.3.1 Ask user for new ID, CD Title and Artist
        lstTplUserInputs = IO.add()

        # 3.3.2 Add item to the table
        #TODO move code into function
        for item in lstTplUserInputs:
            intID = int(item[0])
            strTitle = item[1]
            strArtist = item[2]
            CDobj = CD(intID, strTitle, strArtist)
            lstOfCDObjects.append(CDobj)
        IO.show_inventory(lstOfCDObjects)
        #TODO flag end

    # 3.4 process save inventory to file
            # let user save inventory to file
    elif strChoice == 'SAVE':

        # 3.4.1 display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()

        # 3.4.2 Process choice
        if strYesNo == 'y':

            # 3.4.2.1 save data
            FileIO.save_inventory(strFileName, lstOfCDObjects)

        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.

        # let user load inventory from file
    # 3.5 process load inventory
    elif strChoice == 'LOAD':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' (case sensitive) to continue and reload from file. otherwise reload will be canceled: ')

        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = FileIO.load_inventory(strFileName)
            IO.show_inventory(lstOfCDObjects)

        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)

    # 3.6 process delete a CD
    elif strChoice == 'DEL':
        # 3.6.1 get Userinput for which CD to delete
        # 3.6.1.1 display Inventory to user
        IO.show_inventory(lstOfCDObjects)
        # 3.6.1.2 ask user which ID to remove

        try:
            intIDDel = int(input('Which ID would you like to delete? ').strip())

        except(ValueError):
            print('Delete ID input must be an integer!')
            continue

        except Exception as e:
            print(e)
            continue

        # 3.6.2 search thru table and delete CD
        DataProcessor.delete_entry(intIDDel, lstOfCDObjects)
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be safe:
    else:
        print('General Error')
