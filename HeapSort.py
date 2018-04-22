# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     HeapSort
   Description :
   Author :       snacker_cc
   date：          2018/4/22
-------------------------------------------------
   Change Activity:
                   2018/4/22:
-------------------------------------------------
"""
__author__ = 'snacker_cc'


class Heap:
    def __init__(self, alist):
        self.heapList = alist

    def swap(self, i, j):
        self.heapList[i], self.heapList[j] = self.heapList[j], self.heapList[i]

    def sink(self, i, j):
        while i*2 <= j:

            k = i*2
            #下沉的思路
                #和下一层最大的元素比较，并交换位置
                #直到和堆的最后一个元素比较完为止
            if(k < j)and(self.heapList[k] < self.heapList[k+1]):
                k = k+1

            if self.heapList[k] < self.heapList[i]:
                break

            self.swap(i, k)
            i = k



    def heapSort(self):

        n = len(self.heapList)-1
#生产堆
        for i in range((int)(n/2), 0, -1):
            self.sink(i, n)

#堆排序
#堆排序的思路是这样的
        #1.交换第一个元素和相对最后一个元素(因为 在之前生产了堆，所以第一个元素一定是最大元素)
        #2.将堆的规模缩小为1到n-1个，（因为最大的哪一个已经确定好了）
        #下沉元素，直到堆的规模为2个为止
        while n>1:
            self.swap(1, n)
            n = n-1
            self.sink(1, n)




















if __name__ == '__main__':

    heap = Heap([0,1,33,44,55,64,11,444,6653,2,999,-111])
    heap.heapSort()
    print(heap.heapList)
















