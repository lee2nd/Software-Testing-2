# Software-Testing-2

1. 迴圈測試 Loop Testing 是一種軟體測試技術，用於驗證程式中的迴圈結構是否能正確運作。在迴圈測試中，目標是檢測迴圈的不同路徑、邊界條件和特殊情況，以確保迴圈能夠正確執行並處理各種情況。
2. Test in isolation (單元測試)的幾個理由
   * 執行速度更快、測試左移(自動化測試成本較低)
   * 故障分析較容易
   * 減少相依性(ex: 數據庫、API、外部服務)
   * 定義良好的單元，使 code 更易於維護、擴展、理解
   * 為回歸測試提供一個安全網，可以預防回歸
   * 團隊合作中可以知道別人弄壞你什麼
   * 促使團隊成員合作，開發者可以獨立處理分配到的單元，不互相干擾
3. 3 個最常需要 mock 的 external dependencies
   * mock API calls
   * mock databases queries
   * mock conditions difficult to generate in a test environment
4. 測試的 function 如果有 random 隨機跳動的結果，可以用 unittest 的 mock 去 fix 住他
5. mock 關鍵 : 寫在 test_ 開頭的那個 py 檔裡面
6. mock 有兩種寫法
   * use decorator
   * use context manager
