# file-idx-searcher
An ground up implementation of file indexer and searcher with python by Tree alg.

### Usage
```bash
python3 file_sql.py <target_dir_to_index> <content_to_search>
```

### Example
```bash
python3 file_sql.py /home/archer/Documents/Python readme

Indexer done, total 6245 file or dirs
Searcher done, /home/archer/Documents/Python/micro-wsgi-server/test/readme
```

### Features
* Python3 implemented
* Increamental Indexer
* Binary search tree backed Indexer
* Support plain file content search _todo_
* Support other sorting and search algorithms