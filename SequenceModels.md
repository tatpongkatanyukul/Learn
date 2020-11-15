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
      * recurrent effect is similar to a deep network: vanishing gradient
      * there is also an exploding gradient. Exploding gradient can be handled easily by **gradient clipping**.
   * Gated Recurrent Unit (GRU)
      * address vanishing gradient (especially in long-term dependency)
      * E.g., The cat, which ate already, was full.
      * gr = sigma( Wr [c(t-1), x(t)] + br ) # relevant gate
      * c'(t) = tanh( Wc [gr * c(t-1), x(t)] + bc )
      * gu = sigma( Wu [c(t-1), x(t)] + bu ) # update gate
      * c(t) = gu * c'(t) + (1 - gu) * c(t-1)
      * c(t) is called 'cell'
      * papers: 
        * Cho et al. 2014. On the properties of neural machine translation: encoder-decoder approaches
        * Chung et al. 2014. Empirical evaluation of Gated Recurrent Neural Networks on Sequence Modeling
   * Long Short-Term Memory (LSTM)
      * c'(t) = tanh( Wc [z(t-1), x(t)] + bc )
      * gu = sigma( Wu [z(t-1), x(t)] + bu )
      * gf = sigma( Wf [z(t-1), x(t)] + bf ) # forget gate
      * go = sigma( Wo [z(t-1), x(t)] + bo )# output gate
      * c(t) = gu * c'(t) + gf * c(t-1)
      * z(t) = go * tanh( c(t) )
   * LSTM with Peephole
      * c'(t) = tanh( Wc [z(t-1), x(t)] + bc )
      * gu = sigma( Wu [z(t-1), x(t), **c(t-1)**] + bu )
      * gf = sigma( Wf [z(t-1), x(t), **c(t-1)**] + bf ) # forget gate
      * go = sigma( Wo [z(t-1), x(t), **c(t-1)**] + bo )# output gate
      * c(t) = gu * c'(t) + gf * c(t-1)
      * z(t) = go * tanh( c(t) )      
   * Bi-directional RNN
      * motivation
        * He said, "Teddy bears are on sale!"
        * He said, "Teddy Roosevelt was a great President."
        * It needs later datapoint (e.g., "on sale" or "president") to determine what Teddy is.
      * Mechanism
        * y(t) = h( Wy [ z(t), z'(t) ] + by )
        * z(t) : forward direction, e.g., z(t) = h( W x(t) + b )
        * z'(t) : backward direction, e.g., z'(t) = h( W **x(T-t+1)** + b )
        * Note: z(t) and z'(t) can be normal RNN, GRU, or LSTM block
      * Drawback
        * need the entire sequence before we can make a prediction, i.e., need to wait until sentence ends.
   * Deep RNNs
      * Sometimes, it is useful to stack layers together to build a more powerful model.
      * x -> z^(1) -> z^(2) -> z^(3) -> y
      
   
## Week 2: Natural Language Processing & Word Embeddings

## Week 3: Sequence models & Attention mechanism
