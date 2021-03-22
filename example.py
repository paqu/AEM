from aem.algorithms.nearest_neighbor import NNStrategy
from aem.instance import Instance


instance  = Instance(NNStrategy())
instance.load_problem("data/kroB100.tsp")
instance.description = "NN, kroB100"
instance.run(50, 50)
instance.save_to_file("results/NN_kroB100.png")
instance.show_stats()