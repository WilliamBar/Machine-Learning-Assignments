(ns lda.data
  (:use (incanter core stats charts io datasets)))

(def s 1000)
(def n 50)
(def m 1)
(def a 1)

(defn random-vector [n min max]
  (sample-uniform n :min min :max max))

(def w1s
  (repeatedly (/ s 2)
              #(concat
                (random-vector m (* -2 a) (- a))
                (random-vector (- n m) (* -2 a) (* 2 a)) [-1])))

(def w2s
  (repeatedly (/ s 2)
              #(concat
                (random-vector m a (* 2 a))
                (random-vector (- n m) (* -2 a) (* 2 a)) [1])))

(def data (matrix (concat w1s w2s)))

(def data-shuffle (matrix (shuffle (concat w1s w2s))))

(defn nonsep-data [mat mc]
  (mult
   mat
   (matrix (shuffle (concat
            (repeat mc (concat (repeat n 1) [-1]))
            (repeat (- s mc) (concat (repeat (+ n 1) 1))))))))
