(define circle-area (lambda (r) (* pi (* r r))))
(circle-area 3)

(define fact (lambda (n) (if (<= n 1) 1 (* n (fact (- n 1))))))
(fact 10)
(fact 12)

(circle-area (fact 5))

(define twice (lambda (x) (* 2 x)))
(twice 5)

(define repeat (lambda (f) (lambda (x) (f (f x)))))
(repeat (twice 5))

(define multi-add (lambda (x y z) (+ x (+ y z))))
(multi-add 10 20 12)
