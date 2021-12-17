#lang racket
; Read input file into list
(define (read-into-list-iter file strings)
  (let ((line (read-line file 'any)))
    (if (eof-object? line)
        strings
        (read-into-list-iter file (append strings (list line))))))

(define (read-into-list file)
  (read-into-list-iter file '()))

(define instructions (call-with-input-file "2021-12-02.txt" read-into-list))

; Problem 1
(displayln "Problem 1:")

(define (parse-instruction instruction)
  (let [(parsed (string-split instruction " "))]
    (cond
      [(string=? (first parsed)
                 "forward")
       (list (string->number (last parsed))0)]
      [(string=? (first parsed)
                 "up")
       (list 0 (* -1 (string->number (last parsed))))]
      [(string=? (first parsed)
                 "down")
       (list 0 (string->number (last parsed)))])))

(define (update-position-iter instructions position i)
  (if (< i (length instructions))
      (update-position-iter instructions
                            (map (lambda (x y)
                                   (+ x y))
                                 position
                                 (parse-instruction (list-ref instructions i)))
                            (+ i 1))
      position))

(define (update-position instructions)
  (update-position-iter instructions '(0 0) 0))

(* (first (update-position instructions))
   (last (update-position instructions)))

; Problem 2
(displayln "Problem 2:")

(define (update-aim-iter instructions position aim i)
  (if (< i (length instructions))
      (let [(instruction (parse-instruction (list-ref instructions i)))]
        (if (= (first instruction) 0)
            ; Adjust aim
            (update-aim-iter instructions
                             position
                             (+ aim
                                (last instruction))
                             (+ i 1))
            ; Adjust position
            (update-aim-iter instructions
                             (list (+ (first position)
                                      (first instruction))
                                   (+ (last position)
                                      (* aim
                                         (first instruction))))
                             aim
                             (+ i 1))))
      position))

(define (update-aim instructions)
  (update-aim-iter instructions '(0 0) 0 0))

(* (first (update-aim instructions))
   (last (update-aim instructions)))