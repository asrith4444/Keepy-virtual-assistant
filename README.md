## Welcome to KEEPY the best virtual assistant

You can use the [editor on GitHub](https://github.com/asrith4444/keepy/edit/master/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```python
import tkinter as tk 
import os
from tqdm import tqdm
from time import sleep
root=tk.Tk() 
  
# setting the windows size
root.title('File Manager') 
root.geometry("650x400") 
menubar = tk.Menu(root) 
  
# Adding File Menu and commands 
file = tk.Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='File', menu = file) 
file.add_command(label ='New File', command = None) 
file.add_command(label ='Open...', command = None) 
file.add_command(label ='Save', command = None) 
file.add_separator() 
file.add_command(label ='Exit', command = root.destroy) 
# declaring string variable 
# for storing name and password 
path_var=tk.StringVar() 
#passw_var=tk.StringVar() 
  
   

def scan(): 
  
    pat=path_entry.get() 
   
      
    #print("The name is : " + name) 
    #print("The password is : " + password) 
    tc=0
    f=0
    pc=0
    bc=0
    oc=0
    tf=0
    # Walking a directory tree and printing the names of the directories and files
    for dirpath, dirnames, files in tqdm(os.walk(pat),desc='loading',unit=' folder'):
        #print(f'Found directory: {dirpath}')
        sleep(.01)
        f=f+1
        for file_name in files:
            tf=tf+1
            if file_name.endswith('.txt'):
                #print('Below files are contaminated with virus')
                #print(file_name)
                tc=tc+1
            elif file_name.endswith('.py'):
                pc=pc+1
            elif file_name.endswith('.bat'):
                bc=bc+1
            else:
                oc=oc+1
    result=tk.Label(root,text='Result:',font=('calibre',10,'bold'))
    result.place(x=50,y=150)
    Rtext=tk.Label(root,text=f'''\nThe no.of folders searched is : {f}\nThe no.of .txt files are : {tc}\nThe no.of .bat files are : {bc}\nThe no.of .py files are : {pc}\nThe other files in the given path is : {oc}\nThe total no.of files in the given directory is : {tf}     ''')
    Rtext.place(x=50,y=175)
    #path_var.set("") 
    #passw_var.set("") 
    
      
    def clearr():
        result.destroy()
        Rtext.destroy()
        path_var.set("")
    clear=tk.Button(root,text = 'Clear', 
                  command = clearr)
    clear.place(x=200,y=125)
# creating a label for  
# name using widget Label 
path_label = tk.Label(root, text = 'Enter the Path', font=('calibre', 10, 'bold')) 
   
# creating a entry for input 
# name using widget Entry 
path_entry = tk.Entry(root, 
                      textvariable = path_var,
                      font=('calibre',10,'normal')) 
   
# creating a label for password 
#passw_label = tk.Label(root, 
#                      text = 'Password', 
#                       font = ('calibre',10,'bold')) 
   
# creating a entry for password 
#passw_entry=tk.Entry(root, 
#                     textvariable = passw_var, 
#                     font = ('calibre',10,'normal'), 
#                     show = '*') 
 
scan=tk.Button(root,text = 'Scan', 
                  command = scan) 
   

title=tk.Label(root, text='File Manager',font=('calibre',30,'bold'),fg='orange')
title.place(x=200,y=20)
head1 = tk.Label(root, text = 'Scan the folders', font=('calibre', 14, 'bold')) 
head1.place(x=50,y=70)
path_label.place(x=50,y=100) 
path_entry.place(x=150,y=100) 

scan.place(x=150,y=125) 
copy=tk.Label(root, text='\u00A9 Copyrights Reserved by AKC',font=('calibre',10,'normal'))
copy.place(x=200,y=375)

root.config(menu = menubar)
root.mainloop() 
```
###This is a part of keepy
