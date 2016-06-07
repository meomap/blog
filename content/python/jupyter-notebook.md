Title: Cài đặt, sử dụng Jupyter Notebook
Date: 2016-06-06 22:00
Authors: htl

## Jupyter là gì?
Là nền tảng tính toán khoa học mã nguồn mở, [interactive](https://en.wikipedia.org/wiki/IPython), hỗ trợ **hơn 40 ngôn ngữ lập trình**, trong đó có **python** (jupyter = **ju**lia + **pyt**hon + **R**). Bài này tập trung vào việc cài đặt, sử dụng jupyter notebook trong lập trình python, cụ thể là giảng dạy python bằng jupyter. Bên cạnh đó, mình thường sử dụng jupyter notebook làm môi trường chạy thử code python ở dạng interactive, trước khi lưu vào script (Biết kết quả từng bước mình làm vẫn thích hơn nhỉ - đó là điểm mạnh của interactive).


## Jupyter notebook
Trước đây là **ipython notebook**, đổi tên thành **jupyter notebook** với mục tiêu hỗ trợ nhiều ngôn ngữ hơn. Là ứng dụng chạy trên nền web cho phép chạy interactive python (tương tự ipython). Hơn thế nữa, nó còn hỗ trợ vẽ các đồ thị, biểu đồ, hỗ trợ viết 1 "notebook" bằng cách sử dụng [Markdown](http://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/Working%20With%20Markdown%20Cells.html)

## Cài đặt jupyter notebook

```Yêu cầu máy đã cài python 3, pip và virtualenv```

### 1. Tạo virtualenv để chạy riêng jupyter:

```
╭─ ~  
╰─$ virtualenv -p $(which python3) jupyter
Running virtualenv with interpreter /usr/local/bin/python3
Using base prefix '/usr/local'
New python executable in /home/htl/jupyter/bin/python3
Also creating executable in /home/htl/jupyter/bin/python
Installing setuptools, pip, wheel...done.
```

### 2. Kích hoạt virtualenv vừa tạo:
```
╭─  ~  
╰─$ source ~/jupyter/bin/activate
(jupyter) ╭─  ~  
╰─$ 
```

### 3. Cài jupyter notebook:

```
(jupyter) ╭─  ~  
╰─$ pip install jupyter notebook
Collecting jupyter
  Using cached jupyter-1.0.0-py2.py3-none-any.whl
Collecting notebook
  Using cached notebook-4.2.1-py2.py3-none-any.whl
Collecting nbconvert (from jupyter)
  Using cached nbconvert-4.2.0-py2.py3-none-any.whl
Collecting qtconsole (from jupyter)
  Using cached qtconsole-4.2.1-py2.py3-none-any.whl
Collecting ipykernel (from jupyter)
  Using cached ipykernel-4.3.1-py2.py3-none-any.whl
Collecting jupyter-console (from jupyter)
  Using cached jupyter_console-4.1.1-py2.py3-none-any.whl
Collecting ipywidgets (from jupyter)
  Using cached ipywidgets-5.1.5-py2.py3-none-any.whl
Collecting jinja2 (from notebook)
  Using cached Jinja2-2.8-py2.py3-none-any.whl
Collecting traitlets (from notebook)
  Using cached traitlets-4.2.1-py2.py3-none-any.whl
Collecting nbformat (from notebook)
  Using cached nbformat-4.0.1-py2.py3-none-any.whl
Collecting jupyter-client (from notebook)
  Using cached jupyter_client-4.2.2-py2.py3-none-any.whl
Collecting tornado>=4 (from notebook)
Collecting terminado>=0.3.3; sys_platform != "win32" (from notebook)
Collecting ipython-genutils (from notebook)
  Using cached ipython_genutils-0.1.0-py2.py3-none-any.whl
Collecting jupyter-core (from notebook)
  Using cached jupyter_core-4.1.0-py2.py3-none-any.whl
Collecting mistune!=0.6 (from nbconvert->jupyter)
  Using cached mistune-0.7.2-py2.py3-none-any.whl
Collecting pygments (from nbconvert->jupyter)
  Using cached Pygments-2.1.3-py2.py3-none-any.whl
Collecting entrypoints (from nbconvert->jupyter)
  Using cached entrypoints-0.2.2-py2.py3-none-any.whl
Collecting ipython>=4.0.0 (from ipykernel->jupyter)
  Using cached ipython-4.2.0-py3-none-any.whl
Collecting widgetsnbextension>=1.2.3 (from ipywidgets->jupyter)
  Using cached widgetsnbextension-1.2.3-py2.py3-none-any.whl
Collecting MarkupSafe (from jinja2->notebook)
Collecting decorator (from traitlets->notebook)
  Using cached decorator-4.0.9-py2.py3-none-any.whl
Collecting jsonschema!=2.5.0,>=2.0 (from nbformat->notebook)
  Using cached jsonschema-2.5.1-py2.py3-none-any.whl
Collecting pyzmq>=13 (from jupyter-client->notebook)
  Using cached pyzmq-15.2.0-cp35-cp35m-manylinux1_x86_64.whl
Collecting ptyprocess (from terminado>=0.3.3; sys_platform != "win32"->notebook)
  Using cached ptyprocess-0.5.1-py2.py3-none-any.whl
Collecting pexpect; sys_platform != "win32" (from ipython>=4.0.0->ipykernel->jupyter)
  Using cached pexpect-4.1.0-py2.py3-none-any.whl
Requirement already satisfied (use --upgrade to upgrade): setuptools>=18.5 in ./jupyter/lib/python3.5/site-packages (from ipython>=4.0.0->ipykernel->jupyter)
Collecting simplegeneric>0.8 (from ipython>=4.0.0->ipykernel->jupyter)
Collecting pickleshare (from ipython>=4.0.0->ipykernel->jupyter)
  Using cached pickleshare-0.7.2-py2.py3-none-any.whl
Collecting backports.shutil-get-terminal-size (from ipython>=4.0.0->ipykernel->jupyter)
  Using cached backports.shutil_get_terminal_size-1.0.0-py2.py3-none-any.whl
Installing collected packages: MarkupSafe, jinja2, decorator, ipython-genutils, traitlets, mistune, pygments, jupyter-core, jsonschema, nbformat, entrypoints, nbconvert, pyzmq, jupyter-client, ptyprocess, pexpect, simplegeneric, pickleshare, backports.shutil-get-terminal-size, ipython, tornado, ipykernel, qtconsole, jupyter-console, terminado, notebook, widgetsnbextension, ipywidgets, jupyter
Successfully installed MarkupSafe-0.23 backports.shutil-get-terminal-size-1.0.0 decorator-4.0.9 entrypoints-0.2.2 ipykernel-4.3.1 ipython-4.2.0 ipython-genutils-0.1.0 ipywidgets-5.1.5 jinja2-2.8 jsonschema-2.5.1 jupyter-1.0.0 jupyter-client-4.2.2 jupyter-console-4.1.1 jupyter-core-4.1.0 mistune-0.7.2 nbconvert-4.2.0 nbformat-4.0.1 notebook-4.2.1 pexpect-4.1.0 pickleshare-0.7.2 ptyprocess-0.5.1 pygments-2.1.3 pyzmq-15.2.0 qtconsole-4.2.1 simplegeneric-0.8.1 terminado-0.6 tornado-4.3 traitlets-4.2.1 widgetsnbextension-1.2.3
(jupyter) ╭─  ~  
╰─$ 
```

### 4. Khởi động jupyter notebook:
```
(jupyter) ╭─  ~  
╰─$ jupyter notebook
[I 21:06:04.603 NotebookApp] Writing notebook server cookie secret to /run/user/1000/jupyter/notebook_cookie_secret
[I 21:06:04.900 NotebookApp] Serving notebooks from local directory: /home/htl
[I 21:06:04.901 NotebookApp] 0 active kernels 
[I 21:06:04.901 NotebookApp] The Jupyter Notebook is running at: http://localhost:8888/
[I 21:06:04.901 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
```

Trình duyệt web mở ra tại địa chỉ: http://localhost:8888 vào môi trường jupyter notebook.

## Sử dụng jupyter cơ bản:

- Bấm **New -> Python 3** để tạo 1 Python 3 notebook mới

- 1 Notebook bao gồm nhiều **cell**, mỗi cell có thể ở dạng **code**, **markdown** hoặc **raw** (thường dùng **code** và **markdown**). Cell có hỗ trợ syntax highlighting tùy vào trạng thái **code** hoặc **markdown**.

- Khi thấy con trỏ nhấp nháy trong cell, bạn đang ở **edit mode**. Để chuyển sang **command mode**, bấm **esc**, khi đó bạn có thể di chuyển giữa các cell bằng các phím mũi tên, hoặc thao tác với các cell bằng các phím tắt như:
```
enter - chuyển sang edit mode
a - insert cell above
b - insert cell below
c - copy cell
x - cut cell
v - paste cell below
shift + v - paste cell above
dd - delete cell
m - chuyển cell sang dạng markdown
y - chuyển cell sang dạng code
l - bật/tắt line number
...
h - bật help để xem phím tắt
```

- Một số phím tắt khi ở **edit mode**:
```
tab/shift + tab - indent/dedent vùng được chọn
shift + tab khi con trỏ ở trong `( )` - hiện help của 1 function, có thể bấm 1, 2, 3, 4 lần để xem chi tiết hơn
hỗ trợ multi-cursor bằng cách giữ ctrl + bấm chuột vào các vị trí cần đặt cursor
```

- Khi đang ở edit mode, muốn xem help mà ko muốn `( )` rồi bấm shift+tab thì gõ `command?`, ví dụ `len?` rồi shift + enter

- Code cell hỗ trợ auto complete code bằng phím **tab**

- Sau khi gõ code trong 1 cell, có thể chạy cell bằng 1 trong các cách:

```
shift+enter: chạy code đó và chọn 1 cell ở dòng dưới (nếu chưa có sẽ tự thêm và chọn cell mới)
alt+enter: chạy code và thêm 1 cell ở dưới
ctrl+enter: chạy code
```

- Ngoài việc chạy được python code, 1 code cell có thể chạy được [magic commands](http://ipython.readthedocs.io/en/stable/interactive/magics.html), hoặc chạy shell command bằng dấu `!`, ví dụ:

```
In [1]: ! cat /etc/passwd

root:x:0:0:root:/root:/bin/zsh
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
```
(Mình đã dùng `!` để chay `wget` và cả `pip` nữa, lol)


Cơ bản đủ để dùng giảng dạy python. Tìm hiểu thêm tại: [ipython documentation](http://ipython.readthedocs.io/en/stable/) hoặc [jupyter documentation](http://jupyter.readthedocs.io/en/latest/)

Happy coding python!

P/S: Có thể dùng jupyter để tạo **file.py** (**New -> Text file**) hoặc bất cứ file gì (tạo xong đổi tên), ví dụ như mình dùng jupyter để tạo **file.md** để viết blog này chẳng hạn.


-htl-