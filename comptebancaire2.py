class Compte_bancaire():
    def __init__(self, titulaire, numero, solde, Type, status, code):

        assert isinstance(titulaire, str) and len(titulaire) >= 0
        assert isinstance(numero, int) and numero >= 0
        assert isinstance(status, bool)
        assert isinstance(solde, float) and solde >= 0
        assert isinstance(code, str) and len(code) == 4
        assert isinstance(Type, str) and (Type == "C" or Type == "E")
        self.titulaire = titulaire
        self.numero = numero
        self.status = status
        self.code = code
        self.solde = solde
        self.type = Type

    def deposer(self, montant):
        assert isinstance(montant, float) and montant >= 0
        if montant > 0:
            self.solde = self.solde + montant
        else:
            print("Operation de dépôt impossible car le montant est inférieur à 0 !")
        return self.solde

    def retirer(self, montant):
        assert isinstance(montant, float) and montant >= 0
        if montant > self.solde:
            print(" Vous ne disposez pas d'une telle somme...")
        else:
            self.solde = self.solde - montant
            print("Retrait de " + str(montant) + " effectué avec succès. Votre nouveau solde est : " + str(self.solde))
        return self.solde

    def verser(self, destinataire, montant):
        assert isinstance(montant, float) and montant >= 0
        assert isinstance(destinataire,Compte_bancaire)
        self.retirer(montant)
        destinataire.deposer(montant)
        print("Operation effectuée avec succès !" + "votre solde a été debité de" + str(
            montant) + "Votre nouveau solde est: " + str(self.solde))
        return self.solde

    def consulter(self):
        print("Votre solde: ", self.solde)
        return self.solde


if __name__ == "__main__":
    c1 = Compte_bancaire("Awa", 1111111, 0.0, "E", True, "1234")
    c2 = Compte_bancaire("Bintou", 1111111, 0.0, "C", True, "4567")
    c1.deposer(500000.0)
    c1.consulter()
    c2.retirer(10000.0)
    c1.verser(c2,300000.0)
    c1.retirer(105000.0)
    c2.retirer(230000.0)
    c1.consulter()
    c2.consulter()
