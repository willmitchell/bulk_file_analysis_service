#ifndef BFAS_ICE
#define BFAS_ICE

module Noblis
{

        sequence<byte> Blob;

        interface BFAS
        {
            Blob analyzeFile(Blob inFile);
        };

};

#endif
