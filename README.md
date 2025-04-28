# asgmt-01-python-for-non-stem
Assignment 01: Python for Non-STEM.

## 練習題指引

- 將練習題的 GitHub Repository 下載到自己的電腦，解壓縮後以 VS Code 開啟專案資料夾。
- 先閱讀 `README.md`，再將答案寫在 `answers.py`
- 練習題共分為三種：
  - 是非題：預設答案 `answer_01 = None`，請以布林型別宣告答案，若覺得是非題的敘述**不正確**，就宣告 `answer_01 = False`，若覺得是非題的敘述**正確**則宣告 `answer_01 = True`
  - 單選題：預設答案 `answer_02 = None`，請以整數型別宣告答案，若覺得單選題的第一個選項**正確**宣告為 `answer_02 = 1`，若覺得單選題的第二個選項**正確**則宣告 `answer_02 = 2`，若覺得單選題的第三個選項**正確**則宣告 `answer_02 = 3`，若覺得單選題的第四個選項**正確**則宣告 `answer_02 = 4`
  - 程式題：以函數/類別宣告答案，函數/類別名稱下的長字串（docstring）會描述測試資料與預期輸出，能夠讓我們充分暸解預期輸入以及預期輸出之間的對應關係，寫作完畢後要記得輸出答案的變數 `return your_answer_variable`
- 如果練習題需要載入檔案，檔案會與練習題存放在同個資料夾中，這時可以運用工作目錄的相對路徑直接指定檔案名稱載入。
- 寫作完成後將 `answers.py` 存檔，再執行專案資料夾中的 `test_runner.py` 進行測試，再依照測試結果修正答案或截圖測試結果繳交作業。

## 01.（是非題）只有 Python 能夠以程式設計做到資料科學的應用。

```python
answer_01 = None
```

## 02.（單選題）下列何者不是現代資料科學，以程式設計實踐資料科學的應用場景？

1. Import
2. Tidy
3. Model
4. Bundle

```python
answer_02 = None
```

## 03.（單選題）下列何者不是寫作、執行 Python 程式的「必備」軟體？

1. 純文字編輯器。
2. 整合開發環境（Integrated Development Environment, IDE）。
3. 終端機。
4. Python 直譯器。 

```python
answer_03 = None
```

## 04.（單選題）下列何者不是本堂課程要安裝的軟體？

1. Anaconda
2. Miniconda
3. VS Code
4. VS Code Python extension

```python
answer_04 = None
```

## 05.（程式題）以函數形式呈現「哈囉世界」。

```python
def answer_05() -> str:
    """
    >>> answer_05()
    'Hello, world!'
    """
```