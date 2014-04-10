(define (merge comp list1 list2)
    (if (null? list1) (list2))
    (if (null? list2) (list1))
    (if (= (car list1) (car list2)) (list (car list1) (merge comp (cdr list1) (cdr list2))))
    (if (comp (car list1) (car list2)) (list (car list1) (merge comp (cdr list1) list2)))
    (if (comp (car list2) (car list1)) (list (car list2) (merge comp list1 (cdr list2)))))

(merge < '(1 5 7 9) '(4 8 10))

(merge > '(9 7 5 1) '(10 8 4 3))
