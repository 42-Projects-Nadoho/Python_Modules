from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.creatures import HealCapability, TransformCapability
from typing import cast


print("\nTesting Creature with healing capability")
healing_factory = HealingCreatureFactory()

print("base:")

base_healer = healing_factory.create_base()
print(base_healer.describe())
print(base_healer.attack())
print(cast(HealCapability, base_healer).heal())

print("evolved:")

evolved_healer = healing_factory.create_evolved()
print(evolved_healer.describe())
print(evolved_healer.attack())
print(cast(HealCapability, evolved_healer).heal())

print("\nTesting Creature with transform capability")
transform_factory = TransformCreatureFactory()

print("base:")

base_transformer = transform_factory.create_base()
print(base_transformer.describe())
print(base_transformer.attack())
print(cast(TransformCapability, base_transformer).transform())
print(base_transformer.attack())
print(cast(TransformCapability, base_transformer).revert())

print("evolved:")

evolved_transformer = transform_factory.create_evolved()
print(evolved_transformer.describe())
print(evolved_transformer.attack())
print(cast(TransformCapability, evolved_transformer).transform())
print(evolved_transformer.attack())
print(cast(TransformCapability, evolved_transformer).revert())
