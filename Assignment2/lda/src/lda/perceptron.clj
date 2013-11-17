(ns lda.perceptron
  (:use (incanter core stats charts io datasets)))

(defn norm [mat]
  (sqrt (sum-of-squares mat)))

(defn create-w' [d]
  (matrix (sample-uniform d)))

(defn delta-x [x]
  (let [cls  (sel x :cols (- (ncol x) 1))]
   (mult cls x )))


(defn update-rho [rho t]
  (rho t))

(defn update-w' [w' rho Y]
  (minus w' (trans (mult rho (reduce plus (matrix (map (comp delta-x matrix) (to-list Y))))))))

(defn correction [w' mat rho k]
  (let [row (sel mat :rows k)]
  (mult (- (last row) (sel (mmult row w') 0 0)) rho row)))

(defn lse [w' mat]
  (/ (sum-of-squares (map #(- (sel (mmult w' ((comp trans matrix) %)) 0 0) (last %)) (to-list mat))) 2))

(defn inc-update-w' [w' rho Y]
  (minus w' (trans (mult rho (delta-x (sel Y :rows 0))))))

(defn misclassify [w' dataset]
  (matrix (filter #(>
             (sel (mult
             (last %)
             (mmult w' ((comp trans matrix) %))) 0 0) 0) (to-list dataset))))

(def data lda.data/data-shuffle)

(defn batch-perceptron [dataset w' Y rho i]
  (cond
   (= (length Y) 0) [w' rho i]
   :else (let [w' (update-w' w' rho Y) Y (misclassify w' dataset) rho (/ 1 (+ 10000 i))] (batch-perceptron dataset w' Y rho (+ i 1)))))

(defn inc-perceptron [dataset w' Y rho i]
  (cond
   (= (length Y) 0) [w' rho i]
   :else (let [w' (inc-update-w' w' rho Y) Y (misclassify w' dataset) rho (/ 1 (+ (/ 1 rho) i))] (inc-perceptron dataset w' Y rho (+ i 1)))))

;; (def rho-i (pmap #(inc-perceptron data w' (misclassify w' data) % 0) (range 0.01 0.05 0.01) ))

(defn pocket-algorithm [dataset w' Y old rho i]
  (loop [w' w' Y Y old old rho rho i i]
    (cond
     (= i 10) (println (str "Stopped at iteration : 100 " ))
     :else (let [w1 (update-w' w' rho Y) y1 (misclassify w' dataset)]
             (cond
              (> (nrow y1) old)
              (do (println (str "Pocket Used, Iterations : "  i  ", misclassified : "  (nrow Y)))
                  (recur w' Y old (/ 1 (+ (/ 1 rho) i)) (+ i 1)))
              :else
              (do (println (str "Iterations : " i ", misclassified : " (nrow y1)))
                  (recur w1 y1 (nrow y1) (/ 1 (+ (/ 1 rho) i)) (+ i 1))))))))

(defn inc-perceptron-loop [dataset w' Y rho i]
   (loop [w' w' Y Y rho rho i i]
     (cond
      (= (length Y) 0) (println (str "Finished at iterations : " i))
      :else (do (println (str "Iterations : " i " , length : "(length Y)))
     (recur (inc-update-w' w' rho Y) (misclassify w' dataset) (/ 1 (+ (/ 1 rho) i)) (+ i 1))))))

(defn least-mean-squares [dataset w' rho i eps]
  (loop [w' w' rho rho i i]
    (let [c (correction w' dataset rho i) w1 (plus w' (trans c)) y1 (misclassify w1 dataset)]
      (cond
       (< (norm c) eps)
      (do (println (str "Correction less than eps, misclassified vectors : " (nrow y1))) w1)
      :else (do (println (str "Iteration : " i ", misclassified vectors : " (nrow y1) ", correction : " (norm c) ", lse : " (lse w1 dataset))) (recur w1 (/ 1 (+ (/ 1 rho) i)) (+ i 1)))))))

(def w' (create-w' 51))
;; (perceptron data w' (misclassify w' data) 10000 0)
