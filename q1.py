"""
Z algorithm 

Author: Harrison Lin 
Version: 02/04/2023

"""

import sys

def z_Algorithm(pat, text):
    """
    This function is a string matching function, which will takes only linear time for 
    the complexity, this function will find all the occurence of the pattern "pat" in 
    the text "text". Returns a list of matching numbers in corresponding location.

    :param : the String of text and a string of pattern, which will be lowercase letters 
    :returns : the pattern matched numbers in list 
    :time complexity : O(m+n)
    :space complexity : O(m+n)

    """
    str = pat + "$" + text  # concating pattern and text for searching 
    left, right, n = 0, 0, len(str) 
    # left and right pointers for the searching 
    z = [0] * n  # initial the space to sp
    # SPACE complecity: O(len(pat)+len(text))
    # Time complecity: O(len(pat)+len(text)) -> O(n)
    for i in range(1, n):
        #case1 when the i is less than the right
        if (i > right):
            left, right = i, i # init the left and right same with index 
            while right < n and (str[right] == str[right-left]):
                # check equlity  
                right += 1
            # store the length of pattern matched 
            z[i] = right - left
            right -= 1 
        #case 2: copy from previous matching 
        elif (z[i - left] < (right - i + 1)):
            z[i] = z[i - left]
        #case 3:
        else:
            left = i
            # checking the condition again 
            while right < n and (str[right] == str[right - left]):
                right += 1
            z[i] = right - left
            right -= 1 # reduce right by 1
    return z


def pattern_Matching(text, pat):
    """
    The main function of the queston 1, this function will allow one transposition error 
    The idea of the method is to process the text forward and backwards. And checking the 
    swap by reducing the swap checking with forward and backward list. Becasue this function 
    only allow one place transposition. The comparison will be done by reduce by 2 (see else 
    condition below).

    :param : the String of text and a string of pattern, which will be lowercase letters 
    :returns : the pattern matched numbers in list 
    :time complexity : O(m+n)
    :space complexity : O(m+n)

    """
    
    # open a file and write 
    f = open("output_q1.txt", "w+")
    f.write(" \n \n")  # leave space for total numbers 
    
    m, n = len(pat), len(pat) + len(text) + 1 
    z = z_Algorithm(pat, text)#O(n)
    suffix = z_Algorithm(pat[::-1], text[::-1]) #O(n)

    #reversing the suffix array
    #O(n)
    suffix1 = suffix[0:m+1] #O(n)
    suffix2 = suffix[m+1::] #O(n)
    suffix = suffix1[::-1] + suffix2[::-1]#O(n)
    
    count = 0 #count for file 

    #O(length of the text)
    for i in range(m + 1,n-m+2):
        #Case 1: excat match
        if i < n and m == z[i]:
            # excact match  
            f.write(str(i-m) + "\n")
            count += 1 # wirte to file valid match 
        # Case 2: transposition matching
        else:
            # compare with the reversed z matching list suffix 
            if (i + m -1 ) < n and (m - z[i] - 2) == suffix[i+m-1]:
                # char 1 and char 2 are the digits in pattern and text
                # swap them to get equlity
                char_1 = text[i + z[i] - (m + 1)] == pat[z[i]+1]
                char_2 = text[i + z[i]-m] == pat[z[i]]
                if char_1 and char_2:
                    # writing to the file when condition met 
                    f.write(str(i-m) + " " + str(i + z[i] - m) + "\n")
                    count += 1  # for the total matching 
    #move the file pointer to the beginning                 
    f.seek(0) #O(1) complexity 
    f.write(str(count)+"\n") # writing the number of occurences 
    f.close()


if __name__ =="__main__":
    # system command line 
    _, filename1, filename2 = sys.argv
    text_file = open(filename1, "r")  # text string file
    pat_file = open(filename2, "r")  # pattern string file

    # reading the file and rename it 
    text = text_file.read()
    pat = pat_file.read()

    # close two files 
    text_file.close()
    pat_file.close()
    # run the function, which will create a new file called "output_q1.txt"
    pattern_Matching(text, pat)
