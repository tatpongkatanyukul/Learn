# Sequence Models
a 3-week online course by Andrew Ng, Nov 2020

---

## Week 1: Recurrent Neural Networks
   * Why sequence models
     * c.f. sequential data natively with feedforward network
   * Recurrent Neural Network Model
   * Backpropagation through time
   * Different types of RNNs
     * Many-to-many, many-to-one, one-to-many, one-to-one
     * Many-to-many with Tx = Ty and Many-to-many with Tx != Ty
   * Language model and sequence generation
     * Speech recognition
       * The apple and pair salad / The apple and pear salad
       * P(option 1) = 3.2 x 10^-13 / P(option 2) = 5.7 x 10^-10
       * sentence = y(1), y(2), y(3), ..., y(T)
       * training set: large corpus of english text
         * corpus = large body of text
       * sentence --(tokenize)--> tokens
       * E.g., Cats averages 15 hours of sleep a day <EOS> --> y(1), y(2), ...
       * each y(t) may be a one-hot vector or another type of numerical representation
       * EOS = End-of-Sentence token
       * token ~ represents one of the most commonly used english words
         * The Eggyptian Mau is a bread of cat.<EOS>
         * Mau --> replaced by <unk> or the unknown token
         * MY QUESTION: Are all the new/unknown words getting the same <unk> token or do they have their own? 
  E.g., Mau = unk1, Maui = unk2
       * RNN model for sequence generation: "Cats averages 15 hours of sleep a day <EOS>"
         * a(0) = 0, x(1) = 0, y(1) = 'cat'
         * a(1) = computed, x(2) = y(1), y(2) = 'average'
         * ...
         * y(2) ~ p(average|cat), y(3) ~ p(15|'cat', 'average'), ...
         * time-step cost function: L(yhat(t), y(t)) = -sum_i y_i(t) log yhat_i(t)
         * overall cost: L = sum_t L(yhat(t), y(t))
  
   * Sampling novel sequences
      * Train w/ a(0) = 0, x(1) = 0, x(2) = y(1), x(3) = y(2), ...
      * Use w/ a(0) = 0, x(1) = 0, yhat(1) = softmax --> sample based on yhat(1) --> ypred(1), x(2) = ypred(1), x(3) = ypred(2), ...
   * Vanishing gradients with RNNs
   * Gated Recurrent Unit (GRU)
   * Long Short-Term Memory (LSTM)
   * Bi-directional RNN
   * Deep RNNs
   
## Week 2: Natural Language Processing & Word Embeddings

## Week 3: Sequence models & Attention mechanism
