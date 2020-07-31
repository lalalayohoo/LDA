import matplotlib.pyplot as plt

def graph_draw(topic,perplexity):
    x = topic
    y = perplexity
    plt.plot(x,y,color="red",linewidth=2)
    plt.xlabel("Number of Topic")
    plt.ylabel("Perplexity")
    plt.show()
