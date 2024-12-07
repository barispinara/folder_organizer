from organizer import Organizer

def main():
    test_path = "C:/Users/baris/Desktop/test"
    organizer = Organizer(given_path=test_path)
    organizer.start_organize_files()    

if __name__=="__main__":
    main()