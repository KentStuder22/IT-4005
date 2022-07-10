#This is the twitter function
from Tweet import Tweet
def main():
    #tweet list
    tweet = []
    #file
    fileName = "tweets.dat"

    infile = open(fileName, 'w')
    while( True ):
        print('Tweet Menu\n')
        print('----------\n')
        print('1. Make a Tweet\n')
        print('2. View Recent Tweets\n')
        print('3. Search Tweets\n')
        print('4. Quit\n')

        #getting user input
        try:
            choice = int(input('What would you like to do? '))
            if( choice < 0 or choice > 4 ):
                print('Please select a valid option')
                continue
        except ValueError:
                print('Please enter a valid option')
        else:
            if( choice == 1 ):
                author = input('What is your name? ')
                text = input('What would you like to tweet? ')
                while( len(text) > 140):
                    print('Your tweet has exceeded the 140 character limit')
                    continue
                tweet_object = Tweet(author, text)
                tweet.append(tweet_object)
                print(author, 'your tweet was save.')
            elif( choice == 2 ):
                print('Recent Tweets\n')
                print('-------------\n')
                if( len(tweet) == 0 ):
                    print('There are no recent tweets')
                else:
                    minimum = -1
                    if( len(tweet) > 5 ):
                        minimum = len(tweet) - 6
                    for x in range(len(tweet) - 1, minimum, -1):
                        print(tweet[x])
            elif( choice == 3):
                search = input('What would you like to search for? ')
                key = 0
                for x in range(len(tweet) - 1, -1, -1):
                    if search in tweet[x].get_text():
                        key = 1
                        print(tweet[x])
                if( key == 0):
                    print('No tweets contained ', search)
            elif( choice == 4 ):
                if len(tweet) > 0:
                    outfile = open('tweets.dat', 'a')
                    outfile.close()
                print('Thanks for using the Tweet Manager!')
                break

main ()
            
            
                
