from pysecurecircuit.circuit import Circuit
from pysecurecircuit.server import Server

def main():
    # Create a circuit for two parties
    circuit = Circuit(name="Millionaires' Problem", num_parties=2)

    # Define secure input variables
    alice_wealth = circuit.newSecureInteger()
    bob_wealth = circuit.newSecureInteger()

    # Define the circuit logic
    alice_richer_than_bob = alice_wealth > bob_wealth

    # Assign input variables to parties
    circuit.assign_to_party(party_idx=0, name="Wealth (Alice)", variable=alice_wealth)
    circuit.assign_to_party(party_idx=1, name="Wealth (Bob)", variable=bob_wealth)

    # Set the circuit's output
    circuit.set_output(name="Alice richer than Bob", variable=alice_richer_than_bob)

    # Start the server
    Server(circuit).start()

if __name__ == "__main__":
    main()
