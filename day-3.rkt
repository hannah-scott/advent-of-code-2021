#lang racket
; Problem 1: return gamma * epsilon
(displayln "Problem 1:")

; Determine gamma and epsilon values
(define (get-nth-chars strings pos)
  (map (lambda (x)
         (string (string-ref x pos)))
       strings))

(define (frequency chars pos char)
  (/ (length (filter (lambda (x)
                       (string=? x char))
                     chars))
     (length chars)))

(define (most-frequent-nth strings pos char)
  (define chars (get-nth-chars strings pos))
  (if (> (frequency chars pos char)
         0.5)
      "1"
      "0"))

(define (most-frequent strings output pos char)
  (if (< pos (string-length (first strings)))
      (most-frequent strings
                     (string-append output
                                    (most-frequent-nth strings pos char))
                     (+ pos 1)
                     char)
      output))

(define (determine-gamma strings)
  (most-frequent strings "" 0 "1"))

(define (determine-epsilon strings)
  (most-frequent strings "" 0 "0"))

; Turn binary string into decimal number
(define (bstd-iter s pos sum)
  (if (< pos (string-length s))
      (if (string=? (string (string-ref s pos)) "1")
          (bstd-iter s (+ pos 1) (+ sum (expt 2 (- (string-length s)
                                                   pos
                                                   1))))
          (bstd-iter s (+ pos 1) sum))
      sum))

(define (bin-string-to-dec string)
  (bstd-iter string 0 0))

; Read input file into list
(define (read-into-list-iter file strings)
  (let ((line (read-line file 'any)))
    (if (eof-object? line)
        strings
        (read-into-list-iter file (append strings (list line))))))

(define (read-into-list file)
  (read-into-list-iter file '()))

(define strings (call-with-input-file "day-3.txt" read-into-list))

(* (bin-string-to-dec (determine-gamma strings))
   (bin-string-to-dec (determine-epsilon strings)))

; Problem 2: return oxygen rating * CO2 rating
(displayln "Problem 2:")  

(define (filter-nth-char strings pos char)
  (filter (lambda (s)
            (string=? (string (string-ref s pos))
                      (cond
                        [(= (frequency (get-nth-chars strings pos) pos char) 0.5) char]
                        [(< (frequency (get-nth-chars strings pos) pos char) 0.5) "0"]
                        [else "1"])))
          strings))

(define (determine-oxygen-co2-iter strings pos char)
  (if (= 1 (length strings))
      (first strings)
      (determine-oxygen-co2-iter
       (filter-nth-char strings pos char)
       (+ pos 1)
       char)))

(define (determine-oxygen strings)
  (determine-oxygen-co2-iter strings 0 "1"))

(define (determine-co2 strings)
  (determine-oxygen-co2-iter strings 0 "0"))

(define test-strings (list "00100"
                           "11110"
                           "10110"
                           "10111"
                           "10101"
                           "01111"
                           "00111"
                           "11100"
                           "10000"
                           "11001"
                           "00010"
                           "01010"))

(* (bin-string-to-dec (determine-oxygen strings))
   (bin-string-to-dec (determine-co2 strings)))


                                                   
