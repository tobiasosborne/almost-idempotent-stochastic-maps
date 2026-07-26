# Proof Export

## Node 1

**Statement:** Quotient manifold theorem: if a Lie group G acts smoothly, freely, and properly on a smooth manifold M, then the orbit space M/G is a topological manifold of dimension dim M - dim G with a unique smooth structure for which the quotient map pi:M->M/G is a smooth submersion.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Direct source application of GT-lee-2ed-thm-21.10-corrected: Lee, Theorem 21.10, states that if a Lie group G acts smoothly, freely, and properly on a smooth manifold M, then the orbit space M/G is a topological manifold of dimension dim M - dim G and has a unique smooth structure for which the quotient map pi:M->M/G is a smooth submersion. This is exactly the assertion of node 1; the external preserves the source text byte-for-byte, while M=G, the OCR control glyph between dim M and dim G, and the OCR control glyph before W M ! M=G are respectively the extraction encodings of M/G, the printed minus sign, and pi:M->M/G.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** External-premise bridge: invoke external:GT-lee-2ed-thm-21-10-corrected, a citation-safe alias whose registered source payload is byte-identical to the shard-authorized GT-lee-2ed-thm-21.10-corrected external for Lee, Introduction to Smooth Manifolds, 2nd ed., Theorem 21.10 at refs/lee-smooth-manifolds/lee-smooth-manifolds-2ed.txt:25748-25754. Its verbatim extracted theorem assumes that G is a Lie group acting smoothly, freely, and properly on a smooth manifold M, and concludes that the orbit space is a topological manifold of dimension dim M minus dim G with a unique smooth structure making the quotient map a smooth submersion. Under the shard-authorized OCR decoding M=G -> M/G, control-character 0x06 -> the printed minus sign, and control-character 0x03 W M ! M=G -> pi:M->M/G, the external's hypothesis and conclusion are exactly the hypotheses and conclusion of node 1. Thus node 1.1 follows by direct application of this registered external, with no additional premise.

**Type:** claim

**Inference:** direct_external_theorem_application

**Status:** validated

**Taint:** clean

##### Node 1.1.1.1

**Statement:** Citation-binding and application step. The token external:GT-lee-2ed-thm-21-10-corrected is AF recognized external-citation syntax. Creation of this child succeeds only after AF validates that the cited name resolves to a registered external in this workspace; the registered payload is the shard-authorized verbatim extraction of Lee, Introduction to Smooth Manifolds, 2nd ed., Theorem 21.10 at refs/lee-smooth-manifolds/lee-smooth-manifolds-2ed.txt:25748-25754. The line Externals in scope: (none found) reports only the optional Node.Context and Node.Scope ext-ID metadata, which the current af refine interface neither exposes nor populates from its validated citations; it therefore cannot negate citation registration or the shard authorization. Applying the registered theorem to the Lie group G, smooth manifold M, and the assumed smooth, free, proper action gives exactly that M/G is a topological manifold of dimension dim M - dim G with a unique smooth structure making pi:M->M/G a smooth submersion, after only the shard-authorized OCR readings M=G as M/G, control 0x06 as the printed minus sign, and control 0x03 W M ! M=G as pi:M->M/G. This is precisely node 1.1.1 and hence supplies its claimed direct external-premise bridge without any additional mathematical premise.

**Type:** claim

**Inference:** direct_external_theorem_application_and_AF_citation_binding

**Status:** validated

**Taint:** clean

