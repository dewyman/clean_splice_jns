# This file contains classes for the clean_splice_jns.py program


class IntronBound:

    def __init__(self, transcriptID, jnNumber, ibNumber, chrom, pos, strand, jnStr, genome):
        
        # An ibNumber of 0 signifies that this is the left hand intron boundary of the splice junction (wrt reference genome)
        # An ibNumber of 1 indicates the right hand side.
        self.ID = "__".join([transcriptID, str(jnNumber), str(ibNumber)])
        self.transcriptID = transcriptID
        self.jnNumber = int(jnNumber)
        self.bound = int(ibNumber)
        self.chrom = chrom
        self.pos = int(pos)
        self.strand = strand
        self.isCanonical = True
        if int(jnStr) == 0:
            self.isCanonical = False

    #def isCanonical(self):
    #    return self.isCanonical

    def getBED(self):
        # Format the intron boundary with 0-based start and end. 
        # If mode == "start", we return a bed for the start position.
        
        bedstr = "\t".join([ self.chrom, str(self.pos - 1), str(self.pos), self.ID, "0", self.strand ])
        return bedstr 

    def getSpliceMotif(self, genome):
        if self.bound == 0:
            motif = genome.sequence({'chr': self.chrom, 'start': self.pos, 'stop': self.pos + 1}, one_based=True)
        else:
            motif = genome.sequence({'chr': self.chrom, 'start': self.pos - 1, 'stop': self.pos}, one_based=True)
        return motif
