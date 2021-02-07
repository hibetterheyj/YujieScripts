## python_scripts/download

- **Download all files of given type from url**--`all_files_dl.py` (default types: pdf, zip, rar)

  ```
  - one pdf
      python all_files_dl.py -l https://memento.epfl.ch/academic-calendar/ --save-here
  - many pdf and zip
      python all_files_dl.py -l http://rpg.ifi.uzh.ch/teaching.html --save-here
      # only download zip
      python all_files_dl.py -l http://rpg.ifi.uzh.ch/teaching.html --save-here -t zip
      # only download pdf
      python all_files_dl.py -l http://rpg.ifi.uzh.ch/teaching.html --save-here -t pdf
  ```

  - download all files given a specific type in ubuntu can also use

    ```shell
    # only download zip
    wget -r -l1 -H -t1 -nd -N -np -A.zip -erobots=off http://rpg.ifi.uzh.ch/teaching.html
    # only download pdf
    wget -r -l1 -H -t1 -nd -N -np -A.pdf -erobots=off http://rpg.ifi.uzh.ch/teaching.html
    ```

- **Download all PDFs from url**--`all_pdf_dl.py` (not recommended)

  ```
  - one pdf
      python all_pdf_dl.py -l https://memento.epfl.ch/academic-calendar/ --save-here
  - many pdfs
      python all_pdf_dl.py -l https://idsc.ethz.ch/education/lectures/recursive-estimation.html
  ```

- **Download IROS videos given paper ID**--`IROS_Video_Download.py` (deprecated)