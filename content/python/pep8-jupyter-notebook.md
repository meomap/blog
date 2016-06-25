Title: Check PEP8 trong Jupyter Notebook
Authors: htl

[Jupyter notebook]({filename}jupyter-notebook.md) hỗ trợ rất nhiều chức năng mà bạn có thể tận dụng làm 1 editor, trong đó có show line number (bấm `l` ở `normal mode`) và syntax highlighting. Tuy nhiên, trường hợp bạn muốn check [PEP8](https://www.python.org/dev/peps/pep-0008/) thì jupyter notebook mặc định không hỗ trợ.

Lúc này bạn có thể cài extension của jupyter notebook là **pep8\_magic** để check pep8 ngay trong từng cell.

### 1. Cài extension:
```
%install_ext https://raw.githubusercontent.com/SiggyF/notebooks/master/pep8_magic.py
```
### 2. Load extension trước khi sử dụng:
```
%load_ext pep8_magic
```
### 3. Sử dụng:
```python
%%pep8
# code dưới này
```

-htl-