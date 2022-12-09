;Problem 1 -- Implement function repeat which applies fn to args n times

(define (repeat fn n args)
  (if (= n 0) args
              (repeat fn (- n 1) (get-args fn args))))

(define (get-args fn args) (apply fn args))

;Problem 2 -- Implement iterative-process and last

(define (iterative-process n args fn)
  (last (repeat fn n args)))

(define (last args)
  (if (null? (cdr args)) (car args)
      (last (cdr args))))

;Problem 3 -- Implement f using iterative-process function
(define (f n)
  (iterative-process
       n
       (list 2 1 0)
       (lambda (a b c) (list (+ a (* 2 b) (* 3 c)) a b))))

;Problem 4 -- Rewrite implementation of expt-iter using iterative-process

(define (expt-iter b n)
  (iterative-process
       n
       (list b 1)
       (lambda (a b) (list (* a b) a))))

;Problem 5 -- Write make-iterative-process function

(define make-iterative-process (lambda (args fn) (iterative-process 1 args fn)))
