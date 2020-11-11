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
       * 
      
  
   
   * Sampling novel sequences
   * Vanishing gradients with RNNs
   * Gated Recurrent Unit (GRU)
   * Long Short-Term Memory (LSTM)
   * Bi-directional RNN
   * Deep RNNs
   
## Week 2: Natural Language Processing & Word Embeddings

## Week 3: Sequence models & Attention mechanism
