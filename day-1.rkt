#lang racket
; Read input file of strings into list of numbers
(define (read-into-list-iter file strings)
  (let ((line (read-line file 'any)))
    (if (eof-object? line)
        strings
        (read-into-list-iter file (append strings (list (string->number line)))))))

(define (read-into-list file)
  (read-into-list-iter file '()))

; Count number of times an element is greater than its predecessor
(define (increases-iter lod pos sum)
  (if (< pos (length lod))
      (if (> (list-ref lod pos)
             (list-ref lod (- pos 1)))
          (increases-iter lod (+ pos 1) (+ sum 1))
          (increases-iter lod (+ pos 1) sum))
      sum))

(define (count-increases list-of-depths)
  (increases-iter list-of-depths 1 0))

; From a list, generate a three-point moving sum

; Get sublist, starting at "start" element and "width" elements long
(define (sublist input start width)
  (list-tail (reverse (list-tail (reverse input)
                                 (- (length input)
                                    start
                                    width)))
             start))

(define (moving-sum-iter numbers window pos sums)
  (if (<= (+ pos window) (length numbers))
      (moving-sum-iter numbers
                       window
                       (+ pos 1)
                       (append sums
                               (list (apply + (sublist numbers pos window)))))                                           
      sums))

(define (moving-sum numbers window)
  (moving-sum-iter numbers window 0 '()))

; Put input file into list
(define list-of-depths (call-with-input-file "day-1.txt" read-into-list))

; Problem 1
(displayln "Problem 1:")
(count-increases list-of-depths)

; Problem 2
(displayln "Problem 2:")
(count-increases (moving-sum list-of-depths 3))