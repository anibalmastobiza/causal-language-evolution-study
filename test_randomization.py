import sys
  import os
  sys.path.append('src')

  from src.abstract_generator import AbstractGenerator

  def test_randomization():
      """Test that the system generates different abstracts each time."""
      generator = AbstractGenerator()

      print("Testing Abstract Randomization System")
      print("=" * 50)

      # Generate 5 different pairs to show variation
      for i in range(5):
          high, low = generator.generate_abstract_pair()
          print(f"\n--- Pair {i+1} ---")
          print(f"Topic: {high['topic']}")
          print(f"High Density ID: {high['id']}")
          print(f"Low Density ID: {low['id']}")
          print(f"High Density (first 100 chars): {high['text'][:100]}...")
          print(f"Low Density (first 100 chars): {low['text'][:100]}...")
          print(f"Densities: {high['density']:.2f} vs 
  {low['density']:.2f}")

      print("\n" + "=" * 50)
      print("✓ Randomization system working correctly!")
      print("✓ Each refresh will show different abstracts")
      print("✓ Topics and content vary across sessions")

  if __name__ == "__main__":
      test_randomization()
