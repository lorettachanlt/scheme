

(define (merge comp list1 list2)
  (cond
    ((null? list1) list2)
    ((null? list2) list1)
    ((comp (car list1) (car list2))
     (cons (car list1) (merge comp (cdr list1) list2)))
   		(else (cons (car list2) (merge comp list1 (cdr list2))))))


(merge < '(1 5 7 9) '(4 8 10))
	
(merge > '(9 7 5 1) '(10 8 4 3))
