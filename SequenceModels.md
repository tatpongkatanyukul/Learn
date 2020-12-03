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
      * x -> z^{1} -> z^{2} -> z^{3} -> y
      * Mechanism
        * z^{L}(t) = h( W^{L} [z^{L}(t-1), z^{L-1}(t)] + b^{L})
      * c.f. Feedforward networks (and CNN), 3 layers in RNN seem to be quite a lot (w/ temporal recurrent effect)
      * Or, we may see RNN whose output connects to a deep network (which has no recurrent layer)
   
## Week 2: Natural Language Processing & Word Embeddings

### Word representation

V = [a, aaron, …, zulu, <UNK>]

**1-hot representation**
Man
[0,0,0, …, 1, 0, 0]
Woman
[0,0,0, …, 0, 1, 0]

No relation between 2 different closely related concept.
I want a glass of orange juice.
I want a glass of apple juice.
With 1-hot, orange and apple cannot be related as orange and dog.

**Featurized representation: word embedding**
E.g.

		Man	Woman	King	Queen	Apple	Orange
Gender:	-1	1		-0.95	0.97	0	0
Royal:		0.01	0.02		0.93	0.95	-0.01	0.00
Age:		0.03	0.02		0.7	0.69	0.03	-0.02
Food:		0	0		0	0	0.9	0.92


Visualize word embedding: use t-SNE
(see how clusters relate to similar concepts)

  
### Using word embeddings

Named entity recognition example
E.g.,
input: Sally Johnson is an orange farmer. ; output: 1 1 0 0 0 0.
Robert Lin is an apple farmer.
T K is a durian cultivator. orchardist

Word embedding allows transfer learning: take a lot of unlabeled texts (e.g., words from the internet) to figure out orange, apple, durean are fruits.

Transfer learning and word embeddings
  1. Learn word embeddings from large text corpus (1-100B words)
(or download pre-trained embedding online)
  2. Transfer embedding to new task with smaller training set. (say, 100k) words)
  3. Optional: Continue to finetune the word embeddings with new data.

Word embeddings are useful for named entity recognition, for text summarization, for co-reference resolution, for parsing.
It is less useful for language modeling, machine translation, especially if you're accessing a language modeling or machine translation task for which you have a lot of data just dedicated to that task.

Transfer from some task A to same task B.
The process of transfer learning is just most useful when you happen to have a ton of data for task A and a relatively smaller data set for B.

compare to siamese-twin network: face verificaiton (deepFace)

encoding .... embedding
difference:
  * encoding: learn new encoding from unlimited source
  * embedding: learn embedding and then fixed. Learn from a limited set of words.


### Properties of word embeddings

(Mikolov et al. 2013, Linguistic regularities in continuous space and word representations)

Analogy
E.g.,
Man -> Woman as King -> ?

embed_man - embed_woman = [-2, 0, 0, 0]
embed_king - embed_queen = [-2, 0, 0, 0]

The main difference between man-woman and king-queen is the gender.

embed_man - embed_woman = embed_king - embed_what

Find word w: arg max_w similarity(embed_w, embed_king - embed_man + embed_woman)

similarity: similarity function

The most common similarity function is cosine similarity:
sim(u, v) = u^t v/(||u||_2 ||v||_2).


### Embedding matrix

--> a matrix of (a number of words x a number of features)
--> abbreviated as E.

E dot one-hot vector = feature vector corresponding to that (one-hot) word.

The "feature vector" is called the "embedding."

In practice, we use a sifting operation to get the embedding rather than matrix dot operation, which is inefficient.

### Learning word embeddings

### Word2Vec

### Negative Sampling

### GloVe word vectors
 
### Sentiment Classification

### Debiasing word embeddings

## Week 3: Sequence models & Attention mechanism

### basic model
Image captioning
  * Mao et al. 2014. Deep captioning with multimodal recurrent neural network
  * Vinyals et al. 2014. Show and tell: Neural image caption generator
  * Karpathy and Fei Fei, 2015. Deep visual-semantic alignments for generating image descriptions
  * Image caption, e.g., CNN -> feature -> RNN generates a caption. (See Mao et al. 2014)

Select the most likely sequence
  * MT as conditional probability: P(y(1), y(2), ..., y(Ty)| X)
  * arg max_{y(1),...,y(Ty)} P(y(1), y(2), ..., y(Ty)| X)
  * e.g., **Beam search** to do the optimization
  * Why not a greedy search?
    * Jane is visiting Africa in September.
    * Jane is going to be visiting Africa in September.
    * Perhaps, P(Jane is going|X) > P(Jane is visiting|X).
    
Attention model
  * Bahdanau et al. 2014. Neural machine translation by jointly learning to align and translate.
  * Xu et al. 2015. Show, attend and tell: Neural image caption generation with visual attention. 
