import os,sys,time

def pp(a):
        for b in a + '\n':
                sys.stdout.write(b)
                sys.stdout.flush()
                time.sleep(0.001)

def loading():
        print ('\33[37;1m[\33[32;1m+\33[37;1m] \33[32;1mRunning password on linux ...')
        time.sleep(5)

def logo():
        pp('''
\33[31;1m *******      **      ********  ******** **       **   *******   *******   *******
\33[31;1m/**////**    ****    **//////  **////// /**      /**  **/////** /**////** /**////**
\33[31;1m/**   /**   **//**  /**       /**       /**   *  /** **     //**/**   /** /**    /**
\33[31;1m/*******   **  //** /*********/*********/**  *** /**/**      /**/*******  /**    /**
\33[37;1m/**////   **********////////**////////**/** **/**/**/**      /**/**///**  /**    /**
\33[37;1m/**      /**//////**       /**       /**/**** //****//**     ** /**  //** /**    **
\33[37;1m/**      /**     /** ********  ******** /**/   ///** //*******  /**   //**/*******
\33[37;1m//       //      // ////////  ////////  //       //   ///////   //     // ///////

                    \33[1;33m..:: \33[37;1mPASSWORD V1.0 (4lh4ckXploit) \33[1;33m::..
              \33[37;1m-------------------------------------------------
                          \33[1;33m* \33[31;1mAuthor \33[1;33m: \33[37;1m4lh4ckXploit \33[1;33m*
                      \33[1;33m* \33[31;1mE-mail \33[1;33m: \33[37;1mbdb08*****@gmail.com \33[1;33m*
                \33[1;33m* \33[31;1mGit-hub \33[1;33m: \33[37;1mhttps://github.com/4lh4ckXploit \33[1;33m*
              \33[37;1m-------------------------------------------------''')
loading()
logo()
os.system('python ./create-password-cracker/password.py')
