# 傑克·唐加拉(2021年圖靈獎得主):

## 人物生平：
### 傑克·唐加拉於1972年在芝加哥州立大學獲得數學學士學位，1973年在伊利諾理工學院獲得計算機科學碩士學位，並於1980年在新墨西哥大學獲得應用數學的博士學位，導師為克里夫·莫勒爾

## 研究及職業:
### 唐加拉（Donald J. Dongarra）於1989年成為阿貢國家實驗室高級科學家，專注於線性代數、並行計算、高級計算機體系結構、編程方法和數值算法。他的研究涉及多個開源軟體包和系統，包括EISPACK、LINPACK、BLAS、LAPACK、ScaLAPACK、PVM、MPI、NetSolve、ATLAS、HPCG和PAPI。這些軟體庫在基礎數值算法的準確性、軟體的可靠性和性能方面表現出色，並被廣泛整合到MATLAB、Maple、Wolfram Mathematica、GNU Octave、R語言、SciPy等軟體中，造福廣泛的用戶。唐加拉發表了約300篇文章、論文、報告和技術備忘錄，並在多本書中擔任合著者。他曾在橡樹嶺國家實驗室和曼徹斯特大學任職，自2007年起擔任圖靈研究員。

## 獲獎原因:
### 唐加拉因開創性的概念和方法獲得了圖靈獎，這些概念和方法導致了改變世界的計算。他的算法和軟體被認為推動了高性能計算的發展，並在人工智慧的計算科學到計算機圖形學的許多領域產生了重大影響

## 獎項及榮譽:
### 2004年，唐加拉被授予IEEE Sid Fernbach獎，以表彰他在使用創新方法應用高性能計算機方面的貢獻。2008年，他獲得了首屆IEEE可擴展計算卓越獎。

### 2001年，由於對數值軟體，並行和分布式計算，以及問題解決環境的貢獻，他被選為美國國家工程院院士。

### 2021年獲得圖靈獎

## 相關論文:
### 相關連結:https://www.semanticscholar.org/paper/%E4%BB%A4%E4%BA%BA%E9%9C%87%E6%92%BC%E7%9A%84%E5%8F%98%E5%8C%96%E2%80%94%E2%80%94%E5%AF%B9%E8%AF%9D%E6%9D%B0%E5%85%8B%C2%B7%E5%94%90%E5%8A%A0%E6%8B%89-%E7%99%BD%E7%91%9E%E9%9B%AA/b93ea5935144473622c5ea7cf21ac2dac316704d

## 其中一篇是在說明用於影像辨識的深度殘差學習:
### 這項工作提出了一個殘差學習框架，可以簡化比以前使用的更深的網路的訓練，並提供全面的經驗證據，表明這些殘差網路更容易優化，並且可以透過顯著增加的深度來獲得準確性

## 相關程式-訊息傳遞介面(MPI):
### 此範例是由多行程來執行Hello World：
### 這個程式初始化了MPI環境，獲取了當前處理器的名稱，然後印出 "Hello World from " 和處理器名稱。
```
#include <stdio.h>
#include <mpi.h>

int main(int argc, char *argv[])
{
 char processor_name[MPI_MAX_PROCESSOR_NAME];  # processor_name 來存儲處理器的名稱
 int len; # ，len 用於存儲名稱的長度。

 MPI_Init(&argc, &argv); # 這是MPI的初始化函數，用於啟動MPI環境。它接受命令行參數並進行相應的初始化。

 MPI_Get_processor_name(processor_name, &len); # 用於獲取當前處理器的名稱。它將處理器名稱存儲在 processor_name 中，並將名稱的長度存儲在 len 中。
 printf("Hello World from %s\n", processor_name); # 
 
 MPI_Finalize(); # MPI的終止函數
 
 return 0;
}
```
### 執行結果:
```
% mpicc hello.c

% cat nodefile
node1
node2

% mpirun -np 1 -hostfile nodefile a.out（由1節點來執行）
Hello World from node1

% mpirun -np 2 -hostfile nodefile a.out（由2節點來執行）
Hello World from node1
Hello World from node2
```

## 參考連結:
https://zh.wikipedia.org/zh-tw/%E6%9D%B0%E5%85%8B%C2%B7%E5%94%90%E5%8A%A0%E6%8B%89
https://zh.wikipedia.org/wiki/%E8%A8%8A%E6%81%AF%E5%82%B3%E9%81%9E%E4%BB%8B%E9%9D%A2
https://www.semanticscholar.org/paper/%E4%BB%A4%E4%BA%BA%E9%9C%87%E6%92%BC%E7%9A%84%E5%8F%98%E5%8C%96%E2%80%94%E2%80%94%E5%AF%B9%E8%AF%9D%E6%9D%B0%E5%85%8B%C2%B7%E5%94%90%E5%8A%A0%E6%8B%89-%E7%99%BD%E7%91%9E%E9%9B%AA/b93ea5935144473622c5ea7cf21ac2dac316704d
