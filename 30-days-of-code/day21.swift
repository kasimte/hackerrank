# https://www.hackerrank.com/challenges/30-generics/problem
#
# Written in Swift because Python wasn't supported.

import Foundation

struct Printer<T> {
       /**
       *    Name: printArray
       *    Print each element of the generic array on a new line. Do not return anything.
       *    @param A generic array
       **/
       
       // Write your code here
    func printArray(array: [Any]) {
        for a in array {
            print(a)
        }
    }
}


var n = Int(readLine()!)!
var intArray = Array(repeating: 0, count: n);
for i in 0...n - 1 {
    intArray[i] = Int(readLine()!)!;
}

n = Int(readLine()!)!
var stringArray = Array(repeating: "", count: n);
for i in 0...n - 1 {
    stringArray[i] = readLine()!;
}

Printer<Int>().printArray(array: intArray)
Printer<String>().printArray(array: stringArray)