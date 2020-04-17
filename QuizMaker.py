import tkinter as tk
import tkinter.filedialog as fdialog
import os
import codecs

root = tk.Tk()
root.title('quiz maker')
root.geometry('230x270')
root.resizable(0, 0)

msgbox = ''

quiz_name = ''
quiz_qn = 0
quiz_file = r'هنوز انتخاب نشده است'

lbl_name = tk.Label(root, text=':نام سري کوييز را وارد کنيد')
lbl_name.place(x=50, y=10)
entry_name = tk.Entry(root)
entry_name.place(x=50, y=40)

lbl_qn = tk.Label(root, text=':تعداد سوالات کوييز را وارد کنيد')
lbl_qn.place(x=30, y=70)
entry_qn = tk.Entry(root)
entry_qn.place(x=50, y=100)

def onEnter(event):
    global root
    global msgbox
    global quiz_file
    msgbox = tk.Toplevel(root)
    lbl_msg = tk.Label(msgbox, text=quiz_file)
    lbl_msg.grid(row=0, column=0, padx=5, pady=5)

def onLeave(event):
    global msgbox
    msgbox.destroy()

lbl_status = tk.Label(root, text=quiz_file)
lbl_status.place(x=50, y=190)
lbl_status.bind("<Enter>", onEnter)
lbl_status.bind("<Leave>", onLeave)

def clicked(event):
    global quiz_file
    global quiz_qn
    global entry_qn
    ff = fdialog.askopenfile(mode="r", title='فايل خود را انتخاب کنيد', filetypes=[('Text files', '*.txt')])
    quiz_file = str(ff).split('\'')[1]
    lbl_status.config(text=quiz_file)
    lbl_status.place(x=10, y=190)
    quiz_qn = int(entry_qn.get())

def exporthtml(event):
    global quiz_qn
    global quiz_file
    print('start')
    with codecs.open('index.html', 'a', encoding='utf8') as out:
        out.write('<!DOCTYPE html>\n<html>\n\n<head>\n\t<meta charset=\"utf-8\">\n\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, shrink-to-fit=no\">\n\t<title>سامانه کوییز آنلاین</title>\n\t')
        out.write('<link rel=\"stylesheet\" href=\"assets/bootstrap/css/bootstrap.min.css\">\n\t<link rel=\"stylesheet\" href=\"https://fonts.googleapis.com/css?family=Bitter:400,700\">\n\t')
        out.write('<link rel=\"stylesheet\" href=\"assets/fonts/font-awesome.min.css\">\n\t<link rel=\"stylesheet\" href=\"assets/css/Footer-Dark.css\">\n\t<link rel=\"stylesheet\" href=\"assets/css/Header-Dark.css\">\n\t')
        out.write('<link rel=\"stylesheet\" href=\"assets/css/styles.css\">\n\t<script language=\"Javascript\">\n\t\tfunction download(q1')
        for i in range(2, quiz_qn+1):
            out.write(', q' + str(i))
        out.write(') {\n\t\t\t')
        out.write('var pom = document.createElement(\'a\');\n\t\t\t')
        out.write('pom.setAttribute(\'href\', \'data:text/plain;charset=utf-8,\' ')
        for i in range(1, quiz_qn+1):
            out.write('+ encodeURIComponent(\'#')
            out.write(str(i))
            out.write(':\')')
            out.write('+ encodeURIComponent(q')
            out.write(str(i))
            out.write(')')
            out.write('+ \'\\n\\n\'')
        out.write(');\n\t\t\t')
        out.write('pom.setAttribute(\'download\', \'quiz\');\n\n\t\t\t')
        out.write('pom.style.display = \'none\';\n\t\t\t')
        out.write('document.body.appendChild(pom);\n\n\t\t\t')
        out.write('pom.click();\n\n\t\t\t')
        out.write('document.body.removeChild(pom);\n\t\t}\n\n\t\t')
        out.write('function addTextHTML() {\n\t\t\t')
        out.write('document.addtext.name.value = document.addtext.name.value + \".html\"\n\t\t}\n\t</script>\n</head>\n\n')
        
        out.write('<body>\n\t<form action=\".\QuizTip\index.html\" name=\"addtext\" method=\"POST\" onsubmit=\"download(this[\'q1\'].value')
        for i in range(2, quiz_qn+1):
            out.write(', this[\'q')
            out.write(str(i))
            out.write('\'].value')
        out.write(')">\n\t\t<div class="header-dark">\n\t\t\t<nav class="navbar navbar-dark navbar-expand-md navigation-clean-search">\n\t\t\t\t<div class=\"container\"><a class=\"navbar-brand\" href=\"#\">')
        out.write('کوييز سري ')
        out.write(entry_name.get())
        out.write('</a><button data-toggle=\"collapse\" class=\"navbar-toggler\" data-target=\"#navcol-1\"><span class=\"sr-only\">Toggle navigation</span><span class=\"navbar-toggler-icon\"></span></button>\n\t\t\t\t\t')
        out.write('<div class=\"collapse navbar-collapse\" id=\"navcol-1\">\n\t\t\t\t\t\t')
        out.write('<form class=\"form-inline mr-auto\" target=\"_self\">\n\t\t\t\t\t\t\t')
        out.write('<div class=\"form-group\"><label for=\"search-field\"><i class=\"fa fa-pencil\"></i></label></div>\n\t\t\t\t\t\t</form>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</nav>\n\t\t\t')

        out.write('<div class=\"container hero\">\n\t\t\t\t<div class=\"row\">\n\t\t\t\t\t<div class=\"col\">\n')
        
        questions = []
        with codecs.open(quiz_file, 'r', encoding='utf8') as rd:
            questions = rd.readlines()
            rd.close()
        questions = [x.strip() for x in questions]
        #questions = questions[::-1]
        questions.insert(0, '')
        
        #Cards of questions
        for i in range(1, quiz_qn+1):
            out.write('\t\t\t\t\t<div class=\"card\">\n\t\t\t\t\t\t<div class=\"card-body\">\n\t\t\t\t\t\t\t')
            out.write('<h4 class=\"card-title\" style=\"float:right;\">')
            out.write('پرسش شماره ')
            out.write(str(i))
            out.write('</h4>\n\t\t\t\t\t\t\t')
            out.write('<p class=\"card-text\" style=\"float:right; direction: rtl;\"><br><br>')
            out.write(questions[i])
            out.write('<br><br></p><textarea style=\"direction: rtl;\" name=\"q')
            out.write(str(i))
            out.write('\" placeholder=\"جواب خود را در این قسمت بنویسید\"></textarea></div>\n\t\t\t\t\t</div>\n\t\t\t\t\t<hr style="color: transparent;">\n\n')

        out.write('\t\t\t\t\t<button class="btn btn-primary" type="submit">اتمام کوییز</button></div>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\t</form>\n\t')

        out.write('<div class=\"footer-dark\">\n\t\t<footer>\n\t\t\t<div class=\"container\">\n\t\t\t\t<div class=\"row\">\n\t\t\t\t\t<div class=\"col-sm-6 col-md-3 item\">\n\t\t\t\t\t\t')
        out.write('<h3>خدمات</h3>\n\t\t\t\t\t\t<ul>\n\t\t\t\t\t\t\t<li>سامانه کوییز آنلاین</li>\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t</div>\n\t\t\t\t\t')
        out.write('<div class=\"col-sm-6 col-md-3 item\">\n\t\t\t\t\t\t<h3>درباره ما</h3>\n\t\t\t\t\t\t<ul>\n\t\t\t\t\t\t\t<li>تیم انباری</li>\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t</div>\n\t\t\t\t\t')
        out.write('<div class=\"col-md-6 item text\">\n\t\t\t\t\t\t<h3>انباری</h3>\n\t\t\t\t\t\t<p>تیم طراحی انباری</p>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t<p class=\"copyright\">Anbari copyright © 2020</p>')
        out.write('\n\t\t\t</div>\n\t\t</footer>\n\t</div>\n\t<script src=\"assets/js/jquery.min.js\"></script>\n\t<script src=\"assets/bootstrap/js/bootstrap.min.js\"></script>\n</body>\n\n</html>')
    print('done')

lbl_quizfile = tk.Label(root, text=':فايل متن کوييز را انتخاب کنيد')
lbl_quizfile.place(x=35, y=130)

btn_choosefile = tk.Button(root, text='Browse...')
btn_choosefile.bind("<Button-1>", clicked)
btn_choosefile.place(x=80, y=160)

btn_export = tk.Button(root, text='ساخت فايل هاي کوييز')
btn_export.bind("<Button-1>", exporthtml)
btn_export.place(x=50, y=220)


#tk.mainloop()
