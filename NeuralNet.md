# Parameters required and observed by the Neural Network

## Inputs
**Bird_Y** is the Y position of the bird. As it can move only in one axis, the x position does not matter<br>
**TOP_DIST** defines how far the top pipe is from collision with the bird<br>
**BOT_DIST** defines how far the bottom pipe is from collision with the bird<br>
<p> While it is posible for the AI to calculate the distance between the top and bottom pipe, giving these as parameters will help get better results more quickly and efficently. The AI will make decisions based on these inputs to try and optimize its performance in the game.</p>

## Outputs
<p>The decision whether to <strong>Jump()</strong> or take no action is the only interaction the AI has with the game. Consider outputs in the example of a game to be the smallest set of options a player can take, the simplest rules and instructions or what keys they can press to interact with the game. In this case, we have only one output neuron because our actions are limited to a single choice: to jump or not to jump.</p>

## Activation Function
<p>This impacts how we evaluate the output neuron. The activation function used in this neuron is <strong>TanH</strong>, the hyperbolic tan function. This will map output to a scale of -1 to 1 on a hyperbolic curve. 0.5 indicates when the agent should jump.</p>

## Population Size
<p>This value is arbitrary, we will be starting with a population of 100 models per generation.</p>

## Fitness Function
<p>By far the most important parameter of any Neural Network. This is how we improve each generation, and how we ensure which models are the best out of each iteration. Distance, how far the bird travels before game over.</p>

## Max Generations
<p>30 generation limit, this parameter will end the execution eventually regardless of whether we get a perfect model or not.</p>