(ns lda.test
  (:use [lda.perceptron])
  (:use (incanter core stats charts io datasets)))

(misclassify (matrix [0.5 -0.5 0]) (matrix [[1 0 1] [0 1 -1] [-1 0 -1] [0 -1 1]]))

(misclassify (matrix [0.5 0.5 0]) (matrix [[1 0 1] [0 1 -1] [-1 0 -1] [0 -1 1]]))

(misclassify (matrix [-0.5 0.5 0]) (matrix [[1 0 1] [0 1 -1] [-1 0 -1] [0 -1 1]]))
