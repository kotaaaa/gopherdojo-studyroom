# Specification
- Create a command that meets the following specifications
  - Specify a directory
  - Convert JPG files under the specified directory to PNG (default)
  - Recursively process below the directory
  - Can specify image format before and after conversion (optional)
- Please develop the command to meet the following requirements
  - Separate from main package
  - Use only home-made packages, standard packages, and semi-standard packages
  - Semi-standard packages: packages under golang.org/x
  - Create user-defined types
  - Try to generate GoDoc
  - Try to use Go Modules

Translated with www.DeepL.com/Translator (free version)

# How to use
```
$ pwd
(YOUR_PATH)/gopherdojo-studyroom/kadai1/kotaaaa
$ go build -o converter
$ ./converter -path="./testdata/" -srcExt=".jpg" -dstExt=".png"
```

# How to test
```
$ go test ./... --count=1 -cover
?       github.com/kotaaaa/gopherdojo-studyroom/kadai1/kotaaaa  [no test files]
ok      github.com/kotaaaa/gopherdojo-studyroom/kadai1/kotaaaa/convert  8.231s  coverage: 70.4% of statements
ok      github.com/kotaaaa/gopherdojo-studyroom/kadai1/kotaaaa/search   0.005s  coverage: 91.7% of statements
ok      github.com/kotaaaa/gopherdojo-studyroom/kadai1/kotaaaa/validator        0.006s  coverage: 100.0% of statements
```

# Notes 
### Extensions that you can convert to.
- .gif, .jpeg, .jpg, .png

## Help
```
$./converter --help
Usage of /var/folders/nx/xqljz2y954qbyppfwn4w0tcr0000gn/T/go-build027276676/b001/exe/main:
  -dstExt string
        変換後の拡張子 (default ".png")
  -path string
        ファイルパス
  -srcExt string
        変換前の拡張子 (default ".jpg")
exit status 2
```

