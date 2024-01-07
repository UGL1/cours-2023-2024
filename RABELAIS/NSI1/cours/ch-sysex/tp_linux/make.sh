sync

rm -rf HTML/*.html

pandoc -s MD/01_text.md -o HTML/01.html --metadata pagetitle="EX1" --template=uikit2.html
pandoc -s MD/02_text.md -o HTML/02.html --metadata pagetitle="EX2" --template=uikit2.html
pandoc -s MD/03_text.md -o HTML/03.html --metadata pagetitle="EX3" --template=uikit2.html
pandoc -s MD/04_text.md -o HTML/04.html --metadata pagetitle="EX4" --template=uikit2.html
pandoc -s MD/05_text.md -o HTML/05.html --metadata pagetitle="EX5" --template=uikit2.html
pandoc -s MD/06_text.md -o HTML/06.html --metadata pagetitle="EX6" --template=uikit2.html
pandoc -s MD/07_text.md -o HTML/07.html --metadata pagetitle="EX6" --template=uikit2.html

cd VM
zip -r unzip_me *
mv unzip_me.zip ../unzip_me.zip